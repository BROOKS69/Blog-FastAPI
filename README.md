# FastAPI Blog API

A robust, scalable RESTful API for managing users and blog posts, built with FastAPI and MongoDB. This project demonstrates modern backend development practices, including asynchronous operations, secure authentication, and cloud-ready deployment.

## 🚀 Features

- **User Management:** Secure user registration and retrieval with password hashing
- **Blog Management:** Full CRUD operations for blog posts with user association
- **JWT Authentication:** Token-based authentication for protected endpoints
- **MongoDB Integration:** NoSQL database with Beanie ODM for efficient data handling
- **Asynchronous Operations:** Fully async endpoints for high performance
- **Modular Architecture:** Clean separation of concerns with routers, repositories, and schemas
- **Cloud Deployment Ready:** Configured for Vercel serverless deployment with Railway MongoDB
- **Interactive Documentation:** Auto-generated API docs with Swagger UI

## 🛠️ Tech Stack

- **Framework:** FastAPI
- **Database:** MongoDB with Motor (async driver) and Beanie ODM
- **Authentication:** JWT tokens with python-jose
- **Password Hashing:** bcrypt with passlib
- **Deployment:** Vercel (serverless) with Railway (database hosting)
- **Validation:** Pydantic schemas

## 📁 Project Structure

```
├── app/
│   ├── main.py                 # FastAPI application entry point
│   ├── requirements.txt         # Python dependencies
│   ├── blog/
│   │   ├── models.py           # Beanie document models
│   │   ├── schemas.py          # Pydantic request/response schemas
│   │   ├── database.py         # MongoDB connection and initialization
│   │   ├── hashing.py          # Password hashing utilities
│   │   ├── JWTtoken.py         # JWT token creation/verification
│   │   ├── oauth2.py           # OAuth2 authentication dependency
│   │   ├── routers/            # API route handlers
│   │   │   ├── authentication.py
│   │   │   ├── blog.py
│   │   │   └── user.py
│   │   └── repository/         # Business logic layer
│   │       ├── blog.py
│   │       └── user.py
├── vercel.json                 # Vercel deployment configuration
└── README.md
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- MongoDB instance (local or cloud)
- Vercel account (for deployment)

### Local Development

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd fastapi-blog-api
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r app/requirements.txt
   ```

4. **Set environment variables:**
   ```bash
   export MONGODB_URL="mongodb://localhost:27017/blogdb"
   export SECRET_KEY="your-secret-key-here"
   ```

5. **Run the application:**
   ```bash
   uvicorn app.main:app --reload
   ```

6. **Access the API:**
   - API: http://localhost:8000
   - Documentation: http://localhost:8000/docs

### Database Setup

For local development, ensure MongoDB is running. For production, use Railway's free MongoDB service.

## 🚀 Deployment Guide

### Option 1: Railway (Recommended - Full Stack)

Railway provides free hosting for both your app and MongoDB database.

#### 1. Sign up and Create Project
- Go to [railway.app](https://railway.app) and sign up
- Create a new project

#### 2. Add MongoDB Service
- In your project dashboard, click "Add Service"
- Search for "MongoDB" and add it
- Railway will provision a free MongoDB instance
- Copy the `DATABASE_URL` from the MongoDB service variables (it looks like `mongodb://mongo:password@containers-us-west-1.railway.app:1234/railway`)

#### 3. Add Your App Service
- Click "Add Service" again
- Choose "GitHub" to connect your repository
- Select your FastAPI project repository
- Railway will detect it's a Python app

#### 4. Configure Environment Variables
- In your app service, go to "Variables"
- Add:
  - `MONGODB_URL`: Paste the MongoDB connection string from step 2
  - `SECRET_KEY`: Generate a secure random string (e.g., `openssl rand -hex 32`)

#### 5. Deploy
- Railway will automatically build and deploy your app
- Check the deployment logs for any errors
- Once deployed, get the app URL from the service dashboard

#### 6. Test Your API
- Use the Railway app URL + your endpoints (e.g., `https://your-app.railway.app/docs` for docs)
- Test user creation, login, and blog operations

### Option 2: Vercel + Railway MongoDB

If you prefer Vercel's serverless functions:

#### 1. Set up MongoDB on Railway (same as steps 1-2 above)

#### 2. Deploy to Vercel
- Push your code to GitHub
- Go to [vercel.com](https://vercel.com) and sign up
- Click "New Project" and import from GitHub
- Vercel will detect `vercel.json` and configure automatically

#### 3. Set Environment Variables in Vercel
- In project settings > Environment Variables:
  - `MONGODB_URL`: Your Railway MongoDB connection string
  - `SECRET_KEY`: Secure random string

#### 4. Deploy and Test
- Vercel will build and deploy
- Test using the Vercel URL

### Local Testing with Railway MongoDB

To test locally with your Railway database:

1. Copy the `DATABASE_URL` from Railway
2. Set environment variable: `export MONGODB_URL="your-railway-connection-string"`
3. Run locally: `uvicorn app.main:app --reload`
4. Test endpoints as usual

## 📚 API Endpoints

### Authentication
- `POST /login` - User login (returns JWT token)

### Users
- `POST /user` - Create new user
- `GET /user/{id}` - Get user by ID

### Blogs
- `GET /blog` - Get all blogs (authenticated)
- `POST /blog` - Create new blog (authenticated)
- `GET /blog/{id}` - Get blog by ID
- `PUT /blog/{id}` - Update blog (authenticated)
- `DELETE /blog/{id}` - Delete blog (authenticated)

## 🔧 Configuration

### Environment Variables
- `MONGODB_URL`: MongoDB connection string
- `SECRET_KEY`: JWT signing key (generate a secure random string)

### Vercel Configuration
The `vercel.json` file configures the build and routing for serverless deployment.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Credits

- Built with [FastAPI](https://fastapi.tiangolo.com/)
- Database ODM: [Beanie](https://beanie-odm.dev/)
- MongoDB Driver: [Motor](https://motor.readthedocs.io/)
- Authentication: [python-jose](https://python-jose.readthedocs.io/)
- Deployment: [Vercel](https://vercel.com/) & [Railway](https://railway.app/)

## 📞 Support

For questions or issues, please open a GitHub issue or contact the maintainers.
