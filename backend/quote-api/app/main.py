app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3001",  # optional for local testing
        "https://frontend-app--5mgubcy.wittydesert-2d99a67b.westeurope.azurecontainerapps.io"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
