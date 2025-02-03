{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOsIMffjOczFV1yBGmx8+pS",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/saniyagupta03/Intelligent-Database-Agent-for-Automated-SQL-Query-Generation/blob/main/project_1_sql.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Z2jAHwjxhScX",
        "outputId": "40ae3907-6c3f-4a9f-9761-4dc57e626681"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: langchain in /usr/local/lib/python3.11/dist-packages (0.3.16)\n",
            "Collecting langgraph\n",
            "  Downloading langgraph-0.2.69-py3-none-any.whl.metadata (17 kB)\n",
            "Requirement already satisfied: sqlalchemy in /usr/local/lib/python3.11/dist-packages (2.0.37)\n",
            "Collecting streamlit\n",
            "  Downloading streamlit-1.41.1-py2.py3-none-any.whl.metadata (8.5 kB)\n",
            "Requirement already satisfied: PyYAML>=5.3 in /usr/local/lib/python3.11/dist-packages (from langchain) (6.0.2)\n",
            "Requirement already satisfied: aiohttp<4.0.0,>=3.8.3 in /usr/local/lib/python3.11/dist-packages (from langchain) (3.11.11)\n",
            "Requirement already satisfied: langchain-core<0.4.0,>=0.3.32 in /usr/local/lib/python3.11/dist-packages (from langchain) (0.3.32)\n",
            "Requirement already satisfied: langchain-text-splitters<0.4.0,>=0.3.3 in /usr/local/lib/python3.11/dist-packages (from langchain) (0.3.5)\n",
            "Requirement already satisfied: langsmith<0.4,>=0.1.17 in /usr/local/lib/python3.11/dist-packages (from langchain) (0.3.2)\n",
            "Requirement already satisfied: numpy<2,>=1.22.4 in /usr/local/lib/python3.11/dist-packages (from langchain) (1.26.4)\n",
            "Requirement already satisfied: pydantic<3.0.0,>=2.7.4 in /usr/local/lib/python3.11/dist-packages (from langchain) (2.10.6)\n",
            "Requirement already satisfied: requests<3,>=2 in /usr/local/lib/python3.11/dist-packages (from langchain) (2.32.3)\n",
            "Requirement already satisfied: tenacity!=8.4.0,<10,>=8.1.0 in /usr/local/lib/python3.11/dist-packages (from langchain) (9.0.0)\n",
            "Collecting langgraph-checkpoint<3.0.0,>=2.0.10 (from langgraph)\n",
            "  Downloading langgraph_checkpoint-2.0.10-py3-none-any.whl.metadata (4.6 kB)\n",
            "Collecting langgraph-sdk<0.2.0,>=0.1.42 (from langgraph)\n",
            "  Downloading langgraph_sdk-0.1.51-py3-none-any.whl.metadata (1.8 kB)\n",
            "Requirement already satisfied: greenlet!=0.4.17 in /usr/local/lib/python3.11/dist-packages (from sqlalchemy) (3.1.1)\n",
            "Requirement already satisfied: typing-extensions>=4.6.0 in /usr/local/lib/python3.11/dist-packages (from sqlalchemy) (4.12.2)\n",
            "Requirement already satisfied: altair<6,>=4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (5.5.0)\n",
            "Requirement already satisfied: blinker<2,>=1.0.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (1.9.0)\n",
            "Requirement already satisfied: cachetools<6,>=4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (5.5.1)\n",
            "Requirement already satisfied: click<9,>=7.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (8.1.8)\n",
            "Requirement already satisfied: packaging<25,>=20 in /usr/local/lib/python3.11/dist-packages (from streamlit) (24.2)\n",
            "Requirement already satisfied: pandas<3,>=1.4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (2.2.2)\n",
            "Requirement already satisfied: pillow<12,>=7.1.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (11.1.0)\n",
            "Requirement already satisfied: protobuf<6,>=3.20 in /usr/local/lib/python3.11/dist-packages (from streamlit) (4.25.6)\n",
            "Requirement already satisfied: pyarrow>=7.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (17.0.0)\n",
            "Requirement already satisfied: rich<14,>=10.14.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (13.9.4)\n",
            "Requirement already satisfied: toml<2,>=0.10.1 in /usr/local/lib/python3.11/dist-packages (from streamlit) (0.10.2)\n",
            "Collecting watchdog<7,>=2.1.5 (from streamlit)\n",
            "  Downloading watchdog-6.0.0-py3-none-manylinux2014_x86_64.whl.metadata (44 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m44.3/44.3 kB\u001b[0m \u001b[31m1.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in /usr/local/lib/python3.11/dist-packages (from streamlit) (3.1.44)\n",
            "Collecting pydeck<1,>=0.8.0b4 (from streamlit)\n",
            "  Downloading pydeck-0.9.1-py2.py3-none-any.whl.metadata (4.1 kB)\n",
            "Requirement already satisfied: tornado<7,>=6.0.3 in /usr/local/lib/python3.11/dist-packages (from streamlit) (6.4.2)\n",
            "Requirement already satisfied: aiohappyeyeballs>=2.3.0 in /usr/local/lib/python3.11/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain) (2.4.4)\n",
            "Requirement already satisfied: aiosignal>=1.1.2 in /usr/local/lib/python3.11/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain) (1.3.2)\n",
            "Requirement already satisfied: attrs>=17.3.0 in /usr/local/lib/python3.11/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain) (25.1.0)\n",
            "Requirement already satisfied: frozenlist>=1.1.1 in /usr/local/lib/python3.11/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain) (1.5.0)\n",
            "Requirement already satisfied: multidict<7.0,>=4.5 in /usr/local/lib/python3.11/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain) (6.1.0)\n",
            "Requirement already satisfied: propcache>=0.2.0 in /usr/local/lib/python3.11/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain) (0.2.1)\n",
            "Requirement already satisfied: yarl<2.0,>=1.17.0 in /usr/local/lib/python3.11/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain) (1.18.3)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.11/dist-packages (from altair<6,>=4.0->streamlit) (3.1.5)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.11/dist-packages (from altair<6,>=4.0->streamlit) (4.23.0)\n",
            "Requirement already satisfied: narwhals>=1.14.2 in /usr/local/lib/python3.11/dist-packages (from altair<6,>=4.0->streamlit) (1.24.1)\n",
            "Requirement already satisfied: gitdb<5,>=4.0.1 in /usr/local/lib/python3.11/dist-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.12)\n",
            "Requirement already satisfied: jsonpatch<2.0,>=1.33 in /usr/local/lib/python3.11/dist-packages (from langchain-core<0.4.0,>=0.3.32->langchain) (1.33)\n",
            "Requirement already satisfied: msgpack<2.0.0,>=1.1.0 in /usr/local/lib/python3.11/dist-packages (from langgraph-checkpoint<3.0.0,>=2.0.10->langgraph) (1.1.0)\n",
            "Requirement already satisfied: httpx>=0.25.2 in /usr/local/lib/python3.11/dist-packages (from langgraph-sdk<0.2.0,>=0.1.42->langgraph) (0.28.1)\n",
            "Requirement already satisfied: orjson>=3.10.1 in /usr/local/lib/python3.11/dist-packages (from langgraph-sdk<0.2.0,>=0.1.42->langgraph) (3.10.15)\n",
            "Requirement already satisfied: requests-toolbelt<2.0.0,>=1.0.0 in /usr/local/lib/python3.11/dist-packages (from langsmith<0.4,>=0.1.17->langchain) (1.0.0)\n",
            "Requirement already satisfied: zstandard<0.24.0,>=0.23.0 in /usr/local/lib/python3.11/dist-packages (from langsmith<0.4,>=0.1.17->langchain) (0.23.0)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.11/dist-packages (from pandas<3,>=1.4.0->streamlit) (2.8.2)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.11/dist-packages (from pandas<3,>=1.4.0->streamlit) (2024.2)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.11/dist-packages (from pandas<3,>=1.4.0->streamlit) (2025.1)\n",
            "Requirement already satisfied: annotated-types>=0.6.0 in /usr/local/lib/python3.11/dist-packages (from pydantic<3.0.0,>=2.7.4->langchain) (0.7.0)\n",
            "Requirement already satisfied: pydantic-core==2.27.2 in /usr/local/lib/python3.11/dist-packages (from pydantic<3.0.0,>=2.7.4->langchain) (2.27.2)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2->langchain) (3.4.1)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2->langchain) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2->langchain) (2.3.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2->langchain) (2024.12.14)\n",
            "Requirement already satisfied: markdown-it-py>=2.2.0 in /usr/local/lib/python3.11/dist-packages (from rich<14,>=10.14.0->streamlit) (3.0.0)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.11/dist-packages (from rich<14,>=10.14.0->streamlit) (2.18.0)\n",
            "Requirement already satisfied: smmap<6,>=3.0.1 in /usr/local/lib/python3.11/dist-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.2)\n",
            "Requirement already satisfied: anyio in /usr/local/lib/python3.11/dist-packages (from httpx>=0.25.2->langgraph-sdk<0.2.0,>=0.1.42->langgraph) (3.7.1)\n",
            "Requirement already satisfied: httpcore==1.* in /usr/local/lib/python3.11/dist-packages (from httpx>=0.25.2->langgraph-sdk<0.2.0,>=0.1.42->langgraph) (1.0.7)\n",
            "Requirement already satisfied: h11<0.15,>=0.13 in /usr/local/lib/python3.11/dist-packages (from httpcore==1.*->httpx>=0.25.2->langgraph-sdk<0.2.0,>=0.1.42->langgraph) (0.14.0)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.11/dist-packages (from jinja2->altair<6,>=4.0->streamlit) (3.0.2)\n",
            "Requirement already satisfied: jsonpointer>=1.9 in /usr/local/lib/python3.11/dist-packages (from jsonpatch<2.0,>=1.33->langchain-core<0.4.0,>=0.3.32->langchain) (3.0.0)\n",
            "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2024.10.1)\n",
            "Requirement already satisfied: referencing>=0.28.4 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.36.2)\n",
            "Requirement already satisfied: rpds-py>=0.7.1 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.22.3)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.11/dist-packages (from markdown-it-py>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.2)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.11/dist-packages (from python-dateutil>=2.8.2->pandas<3,>=1.4.0->streamlit) (1.17.0)\n",
            "Requirement already satisfied: sniffio>=1.1 in /usr/local/lib/python3.11/dist-packages (from anyio->httpx>=0.25.2->langgraph-sdk<0.2.0,>=0.1.42->langgraph) (1.3.1)\n",
            "Downloading langgraph-0.2.69-py3-none-any.whl (148 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m148.7/148.7 kB\u001b[0m \u001b[31m5.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading streamlit-1.41.1-py2.py3-none-any.whl (9.1 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m9.1/9.1 MB\u001b[0m \u001b[31m47.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading langgraph_checkpoint-2.0.10-py3-none-any.whl (37 kB)\n",
            "Downloading langgraph_sdk-0.1.51-py3-none-any.whl (44 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m44.7/44.7 kB\u001b[0m \u001b[31m3.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading pydeck-0.9.1-py2.py3-none-any.whl (6.9 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m6.9/6.9 MB\u001b[0m \u001b[31m73.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading watchdog-6.0.0-py3-none-manylinux2014_x86_64.whl (79 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m79.1/79.1 kB\u001b[0m \u001b[31m5.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: watchdog, pydeck, langgraph-sdk, streamlit, langgraph-checkpoint, langgraph\n",
            "Successfully installed langgraph-0.2.69 langgraph-checkpoint-2.0.10 langgraph-sdk-0.1.51 pydeck-0.9.1 streamlit-1.41.1 watchdog-6.0.0\n"
          ]
        }
      ],
      "source": []
    },
    {
      "cell_type": "code",
      "source": [
        "import sqlite3\n",
        "\n",
        "def initialize_db():\n",
        "    # Step 1: Connect to SQLite database (file will be created if it doesn't exist)\n",
        "    conn = sqlite3.connect(\"company_db.db\")\n",
        "    cursor = conn.cursor()\n",
        "\n",
        "    # Step 2: Create tables\n",
        "    cursor.execute(\"\"\"\n",
        "        CREATE TABLE IF NOT EXISTS customers (\n",
        "            customer_id INTEGER PRIMARY KEY,\n",
        "            name TEXT NOT NULL,\n",
        "            email TEXT NOT NULL,\n",
        "            phone TEXT,\n",
        "            created_at TEXT DEFAULT CURRENT_TIMESTAMP\n",
        "        );\n",
        "    \"\"\")\n",
        "    cursor.execute(\"\"\"\n",
        "        CREATE TABLE IF NOT EXISTS products (\n",
        "            product_id INTEGER PRIMARY KEY,\n",
        "            product_name TEXT NOT NULL,\n",
        "            price REAL NOT NULL,\n",
        "            stock_quantity INTEGER NOT NULL\n",
        "        );\n",
        "    \"\"\")\n",
        "    cursor.execute(\"\"\"\n",
        "        CREATE TABLE IF NOT EXISTS orders (\n",
        "            order_id INTEGER PRIMARY KEY,\n",
        "            customer_id INTEGER,\n",
        "            product_id INTEGER,\n",
        "            quantity INTEGER NOT NULL,\n",
        "            order_date TEXT DEFAULT CURRENT_TIMESTAMP,\n",
        "            FOREIGN KEY(customer_id) REFERENCES customers(customer_id),\n",
        "            FOREIGN KEY(product_id) REFERENCES products(product_id)\n",
        "        );\n",
        "    \"\"\")\n",
        "\n",
        "    # Step 3: Insert sample data\n",
        "    cursor.executemany(\"\"\"\n",
        "        INSERT INTO customers (name, email, phone) VALUES (?, ?, ?)\n",
        "    \"\"\", [\n",
        "        (\"Alice\", \"alice@example.com\", \"1234567890\"),\n",
        "        (\"Bob\", \"bob@example.com\", \"9876543210\"),\n",
        "        (\"Charlie\", \"charlie@example.com\", \"5555555555\")\n",
        "    ])\n",
        "\n",
        "    cursor.executemany(\"\"\"\n",
        "        INSERT INTO products (product_name, price, stock_quantity) VALUES (?, ?, ?)\n",
        "    \"\"\", [\n",
        "        (\"Laptop\", 1200.50, 10),\n",
        "        (\"Smartphone\", 799.99, 20),\n",
        "        (\"Headphones\", 150.00, 50)\n",
        "    ])\n",
        "\n",
        "    cursor.executemany(\"\"\"\n",
        "        INSERT INTO orders (customer_id, product_id, quantity) VALUES (?, ?, ?)\n",
        "    \"\"\", [\n",
        "        (1, 1, 1),\n",
        "        (2, 2, 2),\n",
        "        (3, 3, 3)\n",
        "    ])\n",
        "\n",
        "    # Step 4: Commit changes and close connection\n",
        "    conn.commit()\n",
        "    conn.close()\n",
        "\n",
        "# Run the function to initialize the database\n",
        "initialize_db()\n",
        "print(\"Database initialized!\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XFdghoDkiANL",
        "outputId": "155db4ad-a3cc-44c3-e688-0da7a89d2524"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Database initialized!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import sqlite3\n",
        "\n",
        "def fetch_all_data():\n",
        "    conn = sqlite3.connect(\"company_db.db\")\n",
        "    cursor = conn.cursor()\n",
        "\n",
        "    print(\"Customers:\")\n",
        "    for row in cursor.execute(\"SELECT * FROM customers\"):\n",
        "        print(row)\n",
        "\n",
        "    print(\"\\nProducts:\")\n",
        "    for row in cursor.execute(\"SELECT * FROM products\"):\n",
        "        print(row)\n",
        "\n",
        "    print(\"\\nOrders:\")\n",
        "    for row in cursor.execute(\"SELECT * FROM orders\"):\n",
        "        print(row)\n",
        "\n",
        "    conn.close()\n",
        "\n",
        "# Fetch data to verify\n",
        "fetch_all_data()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KzH_VDFviGvS",
        "outputId": "b38e18cf-5b3d-4ed2-fb54-fad5fe0cbd34"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Customers:\n",
            "(1, 'Alice', 'alice@example.com', '1234567890', '2025-02-03 06:38:34')\n",
            "(2, 'Bob', 'bob@example.com', '9876543210', '2025-02-03 06:38:34')\n",
            "(3, 'Charlie', 'charlie@example.com', '5555555555', '2025-02-03 06:38:34')\n",
            "\n",
            "Products:\n",
            "(1, 'Laptop', 1200.5, 10)\n",
            "(2, 'Smartphone', 799.99, 20)\n",
            "(3, 'Headphones', 150.0, 50)\n",
            "\n",
            "Orders:\n",
            "(1, 1, 1, 1, '2025-02-03 06:38:34')\n",
            "(2, 2, 2, 2, '2025-02-03 06:38:34')\n",
            "(3, 3, 3, 3, '2025-02-03 06:38:34')\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install langchain_community"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9zb6GuNGivN5",
        "outputId": "0ecc8378-6750-4de3-dae2-dd73f81b4b2c"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting langchain_community\n",
            "  Downloading langchain_community-0.3.16-py3-none-any.whl.metadata (2.9 kB)\n",
            "Requirement already satisfied: PyYAML>=5.3 in /usr/local/lib/python3.11/dist-packages (from langchain_community) (6.0.2)\n",
            "Requirement already satisfied: SQLAlchemy<3,>=1.4 in /usr/local/lib/python3.11/dist-packages (from langchain_community) (2.0.37)\n",
            "Requirement already satisfied: aiohttp<4.0.0,>=3.8.3 in /usr/local/lib/python3.11/dist-packages (from langchain_community) (3.11.11)\n",
            "Collecting dataclasses-json<0.7,>=0.5.7 (from langchain_community)\n",
            "  Downloading dataclasses_json-0.6.7-py3-none-any.whl.metadata (25 kB)\n",
            "Collecting httpx-sse<0.5.0,>=0.4.0 (from langchain_community)\n",
            "  Downloading httpx_sse-0.4.0-py3-none-any.whl.metadata (9.0 kB)\n",
            "Requirement already satisfied: langchain<0.4.0,>=0.3.16 in /usr/local/lib/python3.11/dist-packages (from langchain_community) (0.3.16)\n",
            "Requirement already satisfied: langchain-core<0.4.0,>=0.3.32 in /usr/local/lib/python3.11/dist-packages (from langchain_community) (0.3.32)\n",
            "Requirement already satisfied: langsmith<0.4,>=0.1.125 in /usr/local/lib/python3.11/dist-packages (from langchain_community) (0.3.2)\n",
            "Requirement already satisfied: numpy<2,>=1.22.4 in /usr/local/lib/python3.11/dist-packages (from langchain_community) (1.26.4)\n",
            "Collecting pydantic-settings<3.0.0,>=2.4.0 (from langchain_community)\n",
            "  Downloading pydantic_settings-2.7.1-py3-none-any.whl.metadata (3.5 kB)\n",
            "Requirement already satisfied: requests<3,>=2 in /usr/local/lib/python3.11/dist-packages (from langchain_community) (2.32.3)\n",
            "Requirement already satisfied: tenacity!=8.4.0,<10,>=8.1.0 in /usr/local/lib/python3.11/dist-packages (from langchain_community) (9.0.0)\n",
            "Requirement already satisfied: aiohappyeyeballs>=2.3.0 in /usr/local/lib/python3.11/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain_community) (2.4.4)\n",
            "Requirement already satisfied: aiosignal>=1.1.2 in /usr/local/lib/python3.11/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain_community) (1.3.2)\n",
            "Requirement already satisfied: attrs>=17.3.0 in /usr/local/lib/python3.11/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain_community) (25.1.0)\n",
            "Requirement already satisfied: frozenlist>=1.1.1 in /usr/local/lib/python3.11/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain_community) (1.5.0)\n",
            "Requirement already satisfied: multidict<7.0,>=4.5 in /usr/local/lib/python3.11/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain_community) (6.1.0)\n",
            "Requirement already satisfied: propcache>=0.2.0 in /usr/local/lib/python3.11/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain_community) (0.2.1)\n",
            "Requirement already satisfied: yarl<2.0,>=1.17.0 in /usr/local/lib/python3.11/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain_community) (1.18.3)\n",
            "Collecting marshmallow<4.0.0,>=3.18.0 (from dataclasses-json<0.7,>=0.5.7->langchain_community)\n",
            "  Downloading marshmallow-3.26.0-py3-none-any.whl.metadata (7.3 kB)\n",
            "Collecting typing-inspect<1,>=0.4.0 (from dataclasses-json<0.7,>=0.5.7->langchain_community)\n",
            "  Downloading typing_inspect-0.9.0-py3-none-any.whl.metadata (1.5 kB)\n",
            "Requirement already satisfied: langchain-text-splitters<0.4.0,>=0.3.3 in /usr/local/lib/python3.11/dist-packages (from langchain<0.4.0,>=0.3.16->langchain_community) (0.3.5)\n",
            "Requirement already satisfied: pydantic<3.0.0,>=2.7.4 in /usr/local/lib/python3.11/dist-packages (from langchain<0.4.0,>=0.3.16->langchain_community) (2.10.6)\n",
            "Requirement already satisfied: jsonpatch<2.0,>=1.33 in /usr/local/lib/python3.11/dist-packages (from langchain-core<0.4.0,>=0.3.32->langchain_community) (1.33)\n",
            "Requirement already satisfied: packaging<25,>=23.2 in /usr/local/lib/python3.11/dist-packages (from langchain-core<0.4.0,>=0.3.32->langchain_community) (24.2)\n",
            "Requirement already satisfied: typing-extensions>=4.7 in /usr/local/lib/python3.11/dist-packages (from langchain-core<0.4.0,>=0.3.32->langchain_community) (4.12.2)\n",
            "Requirement already satisfied: httpx<1,>=0.23.0 in /usr/local/lib/python3.11/dist-packages (from langsmith<0.4,>=0.1.125->langchain_community) (0.28.1)\n",
            "Requirement already satisfied: orjson<4.0.0,>=3.9.14 in /usr/local/lib/python3.11/dist-packages (from langsmith<0.4,>=0.1.125->langchain_community) (3.10.15)\n",
            "Requirement already satisfied: requests-toolbelt<2.0.0,>=1.0.0 in /usr/local/lib/python3.11/dist-packages (from langsmith<0.4,>=0.1.125->langchain_community) (1.0.0)\n",
            "Requirement already satisfied: zstandard<0.24.0,>=0.23.0 in /usr/local/lib/python3.11/dist-packages (from langsmith<0.4,>=0.1.125->langchain_community) (0.23.0)\n",
            "Collecting python-dotenv>=0.21.0 (from pydantic-settings<3.0.0,>=2.4.0->langchain_community)\n",
            "  Downloading python_dotenv-1.0.1-py3-none-any.whl.metadata (23 kB)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2->langchain_community) (3.4.1)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2->langchain_community) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2->langchain_community) (2.3.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2->langchain_community) (2024.12.14)\n",
            "Requirement already satisfied: greenlet!=0.4.17 in /usr/local/lib/python3.11/dist-packages (from SQLAlchemy<3,>=1.4->langchain_community) (3.1.1)\n",
            "Requirement already satisfied: anyio in /usr/local/lib/python3.11/dist-packages (from httpx<1,>=0.23.0->langsmith<0.4,>=0.1.125->langchain_community) (3.7.1)\n",
            "Requirement already satisfied: httpcore==1.* in /usr/local/lib/python3.11/dist-packages (from httpx<1,>=0.23.0->langsmith<0.4,>=0.1.125->langchain_community) (1.0.7)\n",
            "Requirement already satisfied: h11<0.15,>=0.13 in /usr/local/lib/python3.11/dist-packages (from httpcore==1.*->httpx<1,>=0.23.0->langsmith<0.4,>=0.1.125->langchain_community) (0.14.0)\n",
            "Requirement already satisfied: jsonpointer>=1.9 in /usr/local/lib/python3.11/dist-packages (from jsonpatch<2.0,>=1.33->langchain-core<0.4.0,>=0.3.32->langchain_community) (3.0.0)\n",
            "Requirement already satisfied: annotated-types>=0.6.0 in /usr/local/lib/python3.11/dist-packages (from pydantic<3.0.0,>=2.7.4->langchain<0.4.0,>=0.3.16->langchain_community) (0.7.0)\n",
            "Requirement already satisfied: pydantic-core==2.27.2 in /usr/local/lib/python3.11/dist-packages (from pydantic<3.0.0,>=2.7.4->langchain<0.4.0,>=0.3.16->langchain_community) (2.27.2)\n",
            "Collecting mypy-extensions>=0.3.0 (from typing-inspect<1,>=0.4.0->dataclasses-json<0.7,>=0.5.7->langchain_community)\n",
            "  Downloading mypy_extensions-1.0.0-py3-none-any.whl.metadata (1.1 kB)\n",
            "Requirement already satisfied: sniffio>=1.1 in /usr/local/lib/python3.11/dist-packages (from anyio->httpx<1,>=0.23.0->langsmith<0.4,>=0.1.125->langchain_community) (1.3.1)\n",
            "Downloading langchain_community-0.3.16-py3-none-any.whl (2.5 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m2.5/2.5 MB\u001b[0m \u001b[31m29.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading dataclasses_json-0.6.7-py3-none-any.whl (28 kB)\n",
            "Downloading httpx_sse-0.4.0-py3-none-any.whl (7.8 kB)\n",
            "Downloading pydantic_settings-2.7.1-py3-none-any.whl (29 kB)\n",
            "Downloading marshmallow-3.26.0-py3-none-any.whl (50 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m50.8/50.8 kB\u001b[0m \u001b[31m4.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading python_dotenv-1.0.1-py3-none-any.whl (19 kB)\n",
            "Downloading typing_inspect-0.9.0-py3-none-any.whl (8.8 kB)\n",
            "Downloading mypy_extensions-1.0.0-py3-none-any.whl (4.7 kB)\n",
            "Installing collected packages: python-dotenv, mypy-extensions, marshmallow, httpx-sse, typing-inspect, pydantic-settings, dataclasses-json, langchain_community\n",
            "Successfully installed dataclasses-json-0.6.7 httpx-sse-0.4.0 langchain_community-0.3.16 marshmallow-3.26.0 mypy-extensions-1.0.0 pydantic-settings-2.7.1 python-dotenv-1.0.1 typing-inspect-0.9.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from langchain import PromptTemplate, LLMChain\n",
        "from langchain.llms import OpenAI\n",
        "\n",
        "\n",
        "# Initialize OpenAI with API key\n",
        "llm = OpenAI(temperature=0, openai_api_key=\"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\")\n",
        "\n",
        "\n",
        "template = \"\"\"\n",
        "You are an expert SQL translator. Translate the following natural language query into a SQL query:\n",
        "Query: {query}\n",
        "\"\"\"\n",
        "\n",
        "prompt = PromptTemplate(template=template, input_variables=[\"query\"])\n",
        "chain = LLMChain(llm=llm, prompt=prompt)\n",
        "\n",
        "def natural_to_sql(nl_query):\n",
        "    try:\n",
        "        sql_query = chain.run({\"query\": nl_query})\n",
        "        return sql_query\n",
        "    except Exception as e:\n",
        "        return str(e)\n",
        "\n",
        "# Test the function\n",
        "nl_query = \"Show all customers who purchased a Laptop.\"\n",
        "sql_query = natural_to_sql(nl_query)\n",
        "print(\"Generated SQL:\", sql_query)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "im_MLFkWicSR",
        "outputId": "15cf085b-7756-4eb5-8456-12d3d7dae00a"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-7-5a866d5041eb>:15: LangChainDeprecationWarning: The class `LLMChain` was deprecated in LangChain 0.1.17 and will be removed in 1.0. Use :meth:`~RunnableSequence, e.g., `prompt | llm`` instead.\n",
            "  chain = LLMChain(llm=llm, prompt=prompt)\n",
            "<ipython-input-7-5a866d5041eb>:19: LangChainDeprecationWarning: The method `Chain.run` was deprecated in langchain 0.1.0 and will be removed in 1.0. Use :meth:`~invoke` instead.\n",
            "  sql_query = chain.run({\"query\": nl_query})\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Generated SQL: Error code: 429 - {'error': {'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, read the docs: https://platform.openai.com/docs/guides/error-codes/api-errors.', 'type': 'insufficient_quota', 'param': None, 'code': 'insufficient_quota'}}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st\n",
        "import sqlite3\n",
        "\n",
        "# Streamlit UI\n",
        "st.title(\"Intelligent Database Agent\")\n",
        "st.text_input(\"Enter your natural language query:\", key=\"query\")\n",
        "\n",
        "if st.button(\"Run Query\"):\n",
        "    nl_query = st.session_state.query\n",
        "    sql_query = natural_to_sql(nl_query)\n",
        "\n",
        "    st.write(\"Generated SQL Query:\")\n",
        "    st.code(sql_query)\n",
        "\n",
        "    # Execute SQL\n",
        "    try:\n",
        "        conn = sqlite3.connect(\"company_db.db\")\n",
        "        cursor = conn.cursor()\n",
        "        cursor.execute(sql_query)\n",
        "        results = cursor.fetchall()\n",
        "        conn.close()\n",
        "\n",
        "        # Display results\n",
        "        st.write(\"Query Results:\")\n",
        "        st.dataframe(results)\n",
        "    except Exception as e:\n",
        "        st.error(f\"Error: {e}\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-NYup7j1k09u",
        "outputId": "4320768c-38ad-4513-bb88-0d5f90fc8eda"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2025-02-03 06:50:55.723 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-03 06:50:55.883 \n",
            "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
            "  command:\n",
            "\n",
            "    streamlit run /usr/local/lib/python3.11/dist-packages/colab_kernel_launcher.py [ARGUMENTS]\n",
            "2025-02-03 06:50:55.888 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-03 06:50:55.891 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-03 06:50:55.896 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-03 06:50:55.900 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-03 06:50:55.901 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-03 06:50:55.905 Session state does not function when running a script without `streamlit run`\n",
            "2025-02-03 06:50:55.910 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-03 06:50:55.911 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-03 06:50:55.912 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-03 06:50:55.914 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-03 06:50:55.919 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-03 06:50:55.921 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-03 06:50:55.922 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!streamlit run app.py\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4jWPJJ03lBBU",
        "outputId": "d28aa03a-467a-460d-f109-2a43d288f4da"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Usage: streamlit run [OPTIONS] TARGET [ARGS]...\n",
            "Try 'streamlit run --help' for help.\n",
            "\n",
            "Error: Invalid value: File does not exist: app.py\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!streamlit run \"project 1-sql.py\""
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Vg1YmAH5lEUO",
        "outputId": "99a98d1a-cbc1-41b3-af78-e13552ee7655"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Usage: streamlit run [OPTIONS] TARGET [ARGS]...\n",
            "Try 'streamlit run --help' for help.\n",
            "\n",
            "Error: Invalid value: File does not exist: project 1-sql.py\n"
          ]
        }
      ]
    }
  ]
}