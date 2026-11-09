# 📘 Session 5: What I Learnt — Retrieval-Augmented Generation (RAG) & Document Intelligence

## 🎯 Objectives
Master the fundamentals of **Retrieval-Augmented Generation (RAG)** by bridging static Large Language Models with external document knowledge. Learn document ingestion, layout parsing, intelligent chunking, semantic embedding vectors, vector databases (Qdrant), and packaging vector search into observable LangChain tools.

---

## 🔑 Key Learnings

### 1. Document Loaders: Docling vs. PyMuPDF4LLM
- **Docling (`langchain-docling`)**:
  - Deep layout-aware parsing using specialized vision and object detection models.
  - Automatically reconstructs reading order, headers, lists, and complex multi-column tables via IBM TableFormer.
  - Can run with `pipeline_options.do_ocr = False` on digital PDFs to accelerate extraction without OCR overhead.
- **PyMuPDF4LLM (`langchain-pymupdf4llm`)**:
  - High-speed markdown conversion directly from PDF text streams.
  - Fast, lightweight, and retains page delimiters (`\n\f`) and structural metadata.

### 2. Intelligent Chunking with `RecursiveCharacterTextSplitter`
- Overcoming fixed-window token limitations by chunking documents into coherent passages.
- Using `chunk_size` (e.g. 1000 characters) and `chunk_overlap` (e.g. 200 characters) to ensure sentence boundaries are preserved across chunk splits and contextual meaning is not severed mid-thought.

### 3. Dense Vector Embeddings (Google Gemini)
- Mapping textual phrases into high-dimensional vector representations using `GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-2")`.
- Vectors capture deep semantic meaning: semantically similar concepts (e.g. "pricing" and "cost") cluster near each other in cosine space, regardless of differing vocabulary.

### 4. Vector Database Architecture (Qdrant Cloud)
- Creating collections with matching dimension sizes and distance metrics (`Distance.COSINE`).
- Configuring resilient network timeouts (`timeout=60.0`) in `QdrantClient` to eliminate `WriteTimeout` exceptions when upserting batches across remote cloud networks.
- Performing similarity search with cosine distance scoring: `similarity_search_with_score(query, k=3)`.

### 5. Packaging RAG into Agent Tools
- Wrapping vector store retrieval into a callable LangChain `@tool`.
- Adding LangSmith `@traceable` decorators for end-to-end observability, tracking query latencies, retrieved chunk snippets, and cosine relevance scores directly in the LangSmith dashboard.
- Giving autonomous agents (`create_agent`) the ability to query document collections on-demand.

---

## 📂 Notebooks & Files in this Directory
- [`session5.ipynb`](./session5.ipynb): Step-by-step notebook covering document loading (Docling & PyMuPDF4LLM), recursive chunking, Gemini embeddings, Qdrant indexing, and building an autonomous RAG agent.
- `paper.pdf` *(local only, git-ignored)*: Sample research paper on multi-class ocular disease recognition and feature fusion used for document ingestion and retrieval evaluation.

