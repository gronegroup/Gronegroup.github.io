# 📧 Configuración de EmailJS para el Sistema de Facturas

## Pasos para configurar el envío de emails

### 1. Crear cuenta en EmailJS
1. Ve a [https://www.emailjs.com/](https://www.emailjs.com/)
2. Haz clic en "Sign Up" (Registrarse)
3. Completa el registro con tu email
4. Verifica tu cuenta desde el email que recibirás

### 2. Configurar Servicio de Email
1. En el dashboard de EmailJS, ve a **Email Services**
2. Haz clic en **Add New Service**
3. Selecciona tu proveedor de email (Gmail, Outlook, etc.)
4. Sigue las instrucciones para conectar tu cuenta
5. **Guarda el Service ID** (ejemplo: `service_abc1234`)

### 3. Crear Template de Email
1. Ve a **Email Templates**
2. Haz clic en **Create New Template**
3. Usa este contenido para el template:

**Subject (Asunto):**
```
Factura #{{invoice_number}} - {{company_name}}
```

**Content (Contenido):**
```
Estimado/a {{client_name}},

Adjuntamos la factura de su compra.

Detalles:
- Número de Factura: {{invoice_number}}
- Fecha: {{invoice_date}}
- Total: {{total}}

Gracias por su compra.

Atentamente,
{{company_name}}
```

4. En la sección de **Settings**, habilita **Attachments**
5. **Guarda el Template ID** (ejemplo: `template_xyz5678`)

### 4. Obtener Public Key
1. Ve a **Account** > **General**
2. Busca la sección **Public Key**
3. **Copia tu Public Key** (ejemplo: `abcdefghijklmn`)

### 5. Actualizar el código
Abre el archivo `invoice-generator.html` y reemplaza estos valores:

**Línea ~359** (Inicialización):
```javascript
emailjs.init("YOUR_PUBLIC_KEY"); // Reemplazar con tu Public Key
```

**Línea ~405** (Envío de email):
```javascript
const response = await emailjs.send(
    'YOUR_SERVICE_ID',      // Reemplazar con tu Service ID
    'YOUR_TEMPLATE_ID',     // Reemplazar con tu Template ID
    templateParams
);
```

### Ejemplo de configuración completa:
```javascript
// Inicialización
emailjs.init("abcdefghijklmn");

// Envío
await emailjs.send(
    'service_abc1234',
    'template_xyz5678',
    templateParams
);
```

## 🎯 Límites del Plan Gratuito
- 200 emails por mes
- Perfecto para comenzar
- Puedes actualizar si necesitas más

## ⚠️ Importante
- No compartas tus claves en repositorios públicos
- El Public Key es seguro usar en el cliente
- El Service ID y Template ID también son seguros

## 🧪 Probar el sistema
1. Abre `index.html` en tu navegador
2. Agrega productos al carrito
3. Completa el checkout con un email válido
4. Envía el pedido por WhatsApp
5. En la factura que se abre, haz clic en "Enviar por Email"
6. Verifica que llegue el email con el PDF adjunto

## 📝 Variables disponibles en el template
- `{{to_email}}` - Email del cliente
- `{{client_name}}` - Nombre del cliente
- `{{invoice_number}}` - Número de factura
- `{{invoice_date}}` - Fecha de emisión
- `{{total}}` - Total con moneda
- `{{company_name}}` - Nombre de la empresa
- `{{pdf_attachment}}` - PDF en base64 (adjunto automático)

## ❓ Problemas comunes

**El email no llega:**
- Verifica que el Service ID y Template ID sean correctos
- Revisa la carpeta de spam del destinatario
- Asegúrate de haber verificado tu cuenta de EmailJS
- Revisa la consola del navegador por errores

**Error de inicialización:**
- Verifica que el Public Key esté correcto
- Asegúrate de que EmailJS esté cargado (script en el head)

**PDF no se adjunta:**
- Verifica que la generación del PDF no tenga errores
- Asegúrate de que el template tenga habilitados los attachments
- El PDF debe ser menor a 2MB en el plan gratuito
