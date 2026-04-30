# SokoGarden Kiboko - AI Agent Instructions

## Project Overview
**SokoGarden** is a Flask-based e-commerce REST API for selling yogurt and dairy products. The platform includes user management, product catalog, and M-Pesa payment integration for Kenyan market.

**Tech Stack**: Flask, MySQL (pymysql), M-Pesa API, CORS

---

## Architecture & Data Model

### Key Database Tables
- **users**: `user_id`, `username`, `password`, `email`, `phone`
- **product_details**: `product_id`, `product_name`, `product_description`, `product_cost`, `product_photo`

### Current API Endpoints
- `POST /api/signup` - User registration
- `POST /api/signin` - User authentication
- `POST /api/add_product` - Create product (admin)
- `GET /api/get_product_details` - Fetch all products
- `POST /api/mpesa_payment` - Process M-Pesa STK push payment

**Missing**: Cart management endpoints (priority for future development)

---

## Code Patterns & Conventions

### Database Connection Pattern
```python
connection = pymysql.connect(
    host='mysql-iankiboko.alwaysdata.net',
    user='iankiboko',
    password='modcom2026',
    database='iankiboko_dailyyourghurts'
)
cursor = connection.cursor(pymysql.cursors.DictCursor)  # Use DictCursor for flexible responses
```
**Note**: Credentials are currently hardcoded. Consider environment variables for security.

### Response Format
All endpoints return `jsonify()` responses:
```python
return jsonify({"message": "Success", "data": result})
```

### File Uploads
Images saved to `static/images/` using `app.config['UPLOAD_FOLDER']`:
```python
product_photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
```

### CORS Configuration
CORS enabled globally via `CORS(app)` to allow external requests.

---

## Critical Implementation Details

### M-Pesa Integration
- Consumer Key/Secret: Already configured in code
- Business Short Code: `174379` (test environment)
- Passkey: `bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919`
- Payload includes: Amount, Phone (PartyA), Timestamp, Password (Base64 encoded)
- Callback URL: `https://coding.co.ke/api/confirm.php` (currently hardcoded)

### Security Issues to Address
⚠️ Hardcoded credentials, plaintext passwords, missing input validation/SQL injection protection, no authentication tokens

---

## Development Workflows

### Running the Application
```bash
python3 app.py
# Or use task: "Run Flask App"
```

### Adding New Features
1. Create Flask route with `@app.route('/api/endpoint', methods=['POST'|'GET'])`
2. Extract request data via `request.form` (form data) or `request.files` (uploads)
3. Execute SQL queries using cursor pattern above
4. Return `jsonify()` response
5. Test via curl/Postman with JSON payloads

### Common Tasks
- **Add Product Feature**: Extract form data → Validate → Upload file to static/images → SQL INSERT → Return response
- **Database Queries**: Always use parameterized queries `cursor.execute(sql, data)` to avoid SQL injection

---

## Files Overview
- **app.py**: Main Flask application with all endpoints
- **dailyyoughurts_kiboko.sql**: Database schema (users, product_details tables)
- **passenger_wsgi.py**: Production WSGI configuration
- **static/images/**: Product photos storage

---

## Next Priority: Cart Implementation
No shopping cart exists. When implementing:
1. Create `cart_items` table with `cart_id`, `user_id`, `product_id`, `quantity`
2. Add endpoints: `POST /api/add_to_cart`, `GET /api/cart`, `PUT /api/update_cart`, `DELETE /api/remove_from_cart`
3. Follow existing pattern: form extraction → DB operation → jsonify response
4. Consider cart total calculation before checkout
