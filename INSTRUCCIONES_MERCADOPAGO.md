# 🚀 Configuración de Mercado Pago - Pagos Automáticos

## ✅ Ya está integrado en tu sitio web

La funcionalidad de pago con Mercado Pago ya está completamente integrada. Solo necesitas completar la configuración.

---

## 📋 Pasos para activar los pagos automáticos

### 1️⃣ Crear cuenta de vendedor en Mercado Pago

1. Ve a: https://www.mercadopago.com.ar
2. Crea una cuenta o inicia sesión
3. Ve a "Tu negocio" → "Configuración"
4. Activa tu cuenta como vendedor

### 2️⃣ Obtener tus credenciales (Access Token)

1. Ingresa al panel de desarrolladores: https://www.mercadopago.com.ar/developers/panel
2. Ve a "Tus aplicaciones" → "Crear aplicación"
3. Selecciona "Pagos online" como tipo de integración
4. Dale un nombre (ej: "Gronegroup Tienda Online")
5. Una vez creada, encontrarás:
   - **Public Key** (comienza con `APP_USR-...`)
   - **Access Token** (comienza con `APP_USR-...`)

### 3️⃣ Configurar las credenciales en tu sitio

Abre el archivo `index.html` y busca la línea **1212** (aproximadamente), donde dice:

```javascript
mercadoPagoAccessToken: 'TU_ACCESS_TOKEN_AQUI', // Reemplaza con tu token real
mercadoPagoPublicKey: 'TU_PUBLIC_KEY_AQUI' // Reemplaza con tu public key
```

Reemplaza `TU_ACCESS_TOKEN_AQUI` y `TU_PUBLIC_KEY_AQUI` con tus credenciales reales:

```javascript
mercadoPagoAccessToken: 'APP_USR-1234567890abcdef-121620-a1b2c3d4e5f6g7h8i9j0-123456789',
mercadoPagoPublicKey: 'APP_USR-a1b2c3d4-1234-5678-9012-a1b2c3d4e5f6'
```

### 4️⃣ Modo de prueba (Opcional - Recomendado)

Antes de activar pagos reales, puedes probar con credenciales de prueba:

1. En el panel de desarrolladores, cambia a "Credenciales de prueba"
2. Usa esas credenciales primero para probar
3. Mercado Pago te dará tarjetas de prueba para simular pagos

---

## 🎯 Cómo funciona

### Para el cliente:

1. Agrega productos al carrito
2. Completa sus datos (nombre, dirección, email, etc.)
3. Selecciona "💳 Pagar con Mercado Pago"
4. Es redirigido al checkout seguro de Mercado Pago
5. Paga con tarjeta, transferencia, efectivo (Rapipago/Pago Fácil), etc.
6. Vuelve a tu sitio con confirmación

### Para vos:

1. Recibirás el dinero en tu cuenta de Mercado Pago
2. Te llega notificación por email del pago
3. Podés ver todos los pagos en el panel de Mercado Pago
4. El dinero se acredita en 24-48hs (tarjeta) o instantáneo (transferencia)

---

## 💰 Comisiones de Mercado Pago

- **Tarjeta de crédito**: ~4.99% + IVA
- **Tarjeta de débito**: ~3.49% + IVA  
- **Dinero en cuenta**: Sin comisión
- **Efectivo (Rapipago/Pago Fácil)**: ~3.99% + IVA

---

## 🔔 Configurar notificaciones (Webhook)

Para recibir notificaciones automáticas de pagos, necesitás configurar un webhook:

1. En el panel de Mercado Pago, ve a "Webhooks"
2. Agrega la URL donde quieras recibir notificaciones
3. Por ahora está configurado: `https://tu-webhook-url.com/notifications`
4. Puedes usar servicios como **Zapier** o **Make.com** para automatizar

---

## 🆘 Soporte

Si tenés problemas:

1. **Documentación oficial**: https://www.mercadopago.com.ar/developers/es/docs
2. **Soporte Mercado Pago**: https://www.mercadopago.com.ar/ayuda
3. **Comunidad de desarrolladores**: https://www.mercadopago.com.ar/developers/es/support

---

## ⚠️ Importante

- **NUNCA** compartas tu Access Token públicamente
- Usa HTTPS en tu sitio (GitHub Pages ya lo tiene)
- Prueba primero con credenciales de prueba
- Verifica los pagos en el panel de Mercado Pago antes de enviar productos

---

## 🎉 ¡Listo!

Una vez configurado, tus clientes podrán pagar automáticamente sin necesidad de WhatsApp. Los pagos se procesarán de forma segura y recibirás el dinero directamente en tu cuenta.
