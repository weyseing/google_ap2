# Setup
- **Obtain a API key from [Google AI Studio](http://aistudio.google.com/apikey)**
- **Copy `.env.example` to `.env` & fill up properties below**
```properties
GOOGLE_API_KEY=
```

- **Create / activate venv**
```bash
uv venv # first-time only
source .venv/bin/activate # activeate
```

- **Install uv packages**
```bash
# sync package
uv sync 

# to check
uv tree 

# to check (local source-code)
uv run python -c "import ap2.types.mandate as m, ap2; print(ap2.__file__, m.__file__, m.CART_MANDATE_DATA_KEY)"
```

