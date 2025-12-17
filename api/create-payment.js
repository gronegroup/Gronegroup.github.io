// Serverless function para crear pagos de Mercado Pago de forma segura
export default async function handler(req, res) {
  // Solo permitir método POST
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Método no permitido' });
  }

  // CORS - permitir que tu sitio web llame a esta función
  res.setHeader('Access-Control-Allow-Credentials', true);
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  try {
    const { items, payer, totalAmount } = req.body;

    // Validar datos recibidos
    if (!items || !payer || !totalAmount) {
      return res.status(400).json({ error: 'Datos incompletos' });
    }

    // Access Token de Mercado Pago (se configura como variable de entorno en Vercel)
    const accessToken = process.env.MERCADO_PAGO_ACCESS_TOKEN;

    if (!accessToken) {
      return res.status(500).json({ error: 'Configuración incompleta del servidor' });
    }

    // Crear preference de pago en Mercado Pago
    const preference = {
      items: items,
      payer: {
        name: payer.name,
        email: payer.email,
        phone: {
          area_code: payer.phone?.substring(0, 4) || '',
          number: payer.phone?.substring(4) || ''
        },
        address: {
          street_name: payer.address || '',
          zip_code: payer.zipCode || ''
        }
      },
      back_urls: {
        success: `${payer.returnUrl}?payment=success`,
        failure: `${payer.returnUrl}?payment=failure`,
        pending: `${payer.returnUrl}?payment=pending`
      },
      auto_return: 'approved',
      external_reference: `ORDER-${Date.now()}`,
      statement_descriptor: 'GRONEGROUP',
      notification_url: process.env.WEBHOOK_URL || undefined
    };

    // Llamar a la API de Mercado Pago
    const response = await fetch('https://api.mercadopago.com/checkout/preferences', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${accessToken}`
      },
      body: JSON.stringify(preference)
    });

    if (!response.ok) {
      const error = await response.json();
      console.error('Error de Mercado Pago:', error);
      return res.status(response.status).json({ 
        error: 'Error al crear la preferencia de pago',
        details: error 
      });
    }

    const data = await response.json();
    
    // Devolver el link de pago al frontend
    return res.status(200).json({
      success: true,
      init_point: data.init_point,
      preference_id: data.id
    });

  } catch (error) {
    console.error('Error en create-payment:', error);
    return res.status(500).json({ 
      error: 'Error interno del servidor',
      message: error.message 
    });
  }
}
