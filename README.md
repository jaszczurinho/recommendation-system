# Hybrid Semantic Recommendation Engine

This project aims to develop an advanced, hybrid recommendation system that leverages LLMs to understand the complex intent behind user queries. 
The system maps unstructured queries into highly structured filters using structured output and combines semantic tag mapping with hard metadata filtering and statistical ranking to deliver personalized and robust recommendations.

## Repository Structure
The project is currently actively developed and follows a modular architecture:

-  **`configuration/`** - Environment variables configurations.
-  **`corpus/`** - Exploration and preprocessing of book descriptions.
-  **`query/`** - Contains the Pydantic models and functions responsible for parsing user input, extracting intent and structured data generation.
-  **`output/`** - Directory storing output data.

## Core Architecture
1. **Intent Extraction**: Using LLMs with structured output and `master_prompt.txt` to parse user queries into structured JSON format.
2. **Semantic Tag Mapping**: To bridge the vocabulary gap between the user and the data set, extracted "soft" concepts (themes, tones) are vectorized. The system then finds the top-k nearest existing tags in the data.
3. **Hybrid Search Pipeline**: Fetching candidate books that match both the user's explicit metadata requirements and the semantically mapped themes/tones.
5. **Multi-Criteria Ranking**: Scoring the retrieved candidates by combining semantic relevance with statistical methods to ensure high-quality recommendations and mitigate popularity bias.

## Roadmap
**Phase 1**: Data exploration - Complete comprehensive data analysis to understand distributions and clean the dataset. <br>
**Phase 2**: Prompt engineering - Design core prompts for reliable intent extraction. <br>
**Phase 3**: Query processing - Implement robust query parsing and validation logic using Pydantic schemas. <br>
**Phase 4**: Semantic mapping - Implement vector embeddings for database tags and logic for top-k similarity matching. <br>
**Phase 5**: Search & ranking algorithm - Implement the hybrid filtering pipeline and scoring logic. <br>
**Phase 6**: User interface - Build an interactive frontend to visualize the recommendation flow.
