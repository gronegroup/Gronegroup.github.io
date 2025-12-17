# Instrucciones de Despliegue en Vercel

## Archivos creados:
- `api/create-payment.js` - Función serverless para crear pagos
- `vercel.json` - Configuración de Vercel

## Pasos para desplegar:

### 1. Subir archivos a GitHub
```bash
git add .
git commit -m "Add Vercel serverless functions for Mercado Pago"
git push origin main
```

### 2. Importar proyecto en Vercel
1. Ve a: https://vercel.com/new
2. Selecciona "Import Git Repository"
3. Busca tu repo: Gronegroup.github.io
4. Click en "Import"

### 3. Configurar variables de entorno
En la pantalla de configuración de Vercel:
1. Click en "Environment Variables"
2. Agrega:
   - Name: `MERCADO_PAGO_ACCESS_TOKEN`
   - Value: `APP_USR-7240877555230620-080518-7bd162ce2b5cc8352ca8a8825aaacd14-451307220`
3. Click en "Deploy"

### 4. Obtener la URL de tu API
Después del deploy, Vercel te dará una URL como:
`https://tu-proyecto.vercel.app`

Tu endpoint de pago será:
`https://tu-proyecto.vercel.app/api/create-payment`

### 5. Actualizar el código del sitio
Reemplaza en `index.html` la llamada al API con la nueva URL de Vercel.
