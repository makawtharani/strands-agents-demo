# Strands Agents - MCP Application Demo

This project is a demonstration of building a Model Context Protocol (MCP) application, created for the AWS User Group Abu Dhabi on July 19, 2025.

## About

This is a proof-of-concept MCP application built with Python that demonstrates how to create both client and server components for the Model Context Protocol. The application showcases integration with various AWS services and tools through the Strands framework.

## Project Structure

```
strands-agents/
├── client/                 # MCP Client implementation
│   └── main.py
├── server/                 # MCP Server implementation  
│   ├── main.py
│   ├── docs.py
│   └── utils.py
├── applications.csv        # Demo data file
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd strands-agents
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   
   On Windows:
   ```bash
   venv\Scripts\activate
   ```
   
   On macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Server

```bash
cd server
python main.py
```

### Running the Client

```bash
cd client  
python main.py
```

## Features

- **MCP Server**: Implements Model Context Protocol server functionality
- **MCP Client**: Demonstrates client-side MCP integration
- **AWS Integration**: Built with AWS services in mind
- **Strands Framework**: Uses the Strands agents framework for enhanced functionality

## Demo Context

This project was created as a live demonstration for the AWS User Group Abu Dhabi meetup, showcasing:
- How to build MCP applications from scratch
- Integration patterns with AWS services
- Client-server architecture for MCP
- Best practices for MCP application development

## Dependencies

Key packages include:
- `fastmcp` - FastMCP framework for building MCP applications
- `strands-agents` - Strands agents framework
- `boto3` - AWS SDK for Python
- `pydantic` - Data validation using Python type annotations
- `starlette` - Lightweight ASGI framework

For a complete list, see `requirements.txt`.

## Contributing

This is a demo project created for educational purposes. Feel free to fork and experiment!

## License

This project is for demonstration purposes. Please check individual dependency licenses for production use.

---

**Created for AWS User Group Abu Dhabi - July 19, 2025** # strands-agents-demo
