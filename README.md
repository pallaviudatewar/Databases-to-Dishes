# Databases-to-Dishes

1. Introduction

A unique feature of human intelligence is the ability to seamlessly combine task-oriented actions with verbal reasoning. Consider the example of cooking up a dish in the kitchen. Between any two specific actions, we may reason in language in order to track progress (“now that everything is cut, I should heat up the pot of water”), to handle exceptions or adjust the plan according to the situation (“I don’t have salt, so let me use soy sauce and pepper instead”), and to realize when external information is needed (“how do I prepare dough? Let me search on the Internet”). The important point of the above quote (and in fact the paper) is the intention to combine two powerful abilities of LLMs reasoning (e.g. chain-of-thought prompting) and acting (e.g. action plan generation). While the former helps with improving the accuracy of an individual task, the latter provides the LLM power to perform multiple tasks. The plan is quite simple ask LLM a question (input) and let it “plan” what to do next (action) by reasoning on the input (thoughts). It can even propose values to the action (action input). Once we perform the action and get an output (observation) the LLM can again reason (thought) to propose the next “plan” (action). In a way, we keep the LLM busy, until it terminates and we get the result we wanted. To summarize we iterate over “input → thoughts → action → action input → observation → thoughts”.
The distinguishing factor of our approach lies in the innovative techniques embedded within Retrieval Augmented Generation. Leveraging advanced algorithms, we have devised a system that not only retrieves relevant data from databases but also generates contextually appropriate content for culinary applications. This dual functionality sets our project apart, offering a comprehensive solution that goes beyond the capabilities of existing methods.

2. Datasets

In order to address the limited availability of high- quality public datasets, we took the initiative to create our own dataset. To accomplish this, we employed web scraping techniques on popular food recipe websites like Allrecipes, Epicurious, Bon Appétit, New York Times Cooking, and others. To navigate the complexities of each website’s structure, we developed custom scrapers tailored to each site. To enhance the robustness of our scraping pro- cess, we integrated advanced techniques such as proxies and headless browsers.

Following data acquisition, we applied preprocessing methods to ensure uniformity and consistency across all the collected data points. This involved transforming the data into a standardized format. As an example of a typical data point within our dataset, imagine a single recipe entry containing information like ingredients, cooking instructions, and other relevant details, all neatly organized and ready for analysis. By creating this comprehensive dataset, we aim to facilitate research and analysis in the realm of food recipes and cooking, making it easier for researchers and enthusiasts to explore culinary data and trends.


3. Methodology

3.1 Data Pre-processing

Following data acquisition, we applied preprocessing methods to ensure uniformity and consistency across all the collected data points. This involved transforming the data into a standardized format. As an example of a typical data point within our dataset, imagine a single recipe entry containing information like ingredients, cooking in- structions, and other relevant details, all neatly organized and ready for analysis. By creating this comprehensive dataset, we aim to facilitate research and analysis in the realm of food recipes and cook- ing, making it easier for researchers and enthusiasts to explore culinary data and trends.

3.2 Implementation of BM25 for Ingredient-Based Search

BM25, a probabilistic retrieval function, is employed to rank recipes based on ingredient similarity. This algorithm is well-suited for handling sparse and unstructured textual data, like ingredients lists.
A custom function is developed to perform ingredient-based searches using the BM25 algorithm. This function takes a list of ingredients as input, processes the query, and returns a ranked list of recipes with the most relevant ingredients.

3.3 Embedding Generation and Vector Store Creation

Embeddings with OpenAI
OpenAIEmbeddings are utilized to convert textual data into numerical representations, capturing semantic similarities. This conversion is essential for effective retrieval and comparison of recipes based on content.

Vector Store with FAISS
FAISS, a library for efficient similarity search, is employed to create a vector store of recipe steps. This store enables quick and relevant retrieval of recipes based on the embeddings generated in the previous step.


Contextual Retrieval and Document Compression

1. Large Language Model (LLM) Setup
An instance of the OpenAI model is initialized, configured to operate with a specific temperature setting. This LLM serves as the backbone for generating and refining recipe content.

2. Document Compression for Relevance
The LLMChainExtractor is implemented to compress and refine the retrieved documents. This step ensures that only the most relevant and concise content is fed into the LLM, enhancing the quality of the generated recipes.

3. Contextual Compression Retrieval
A Contextual Compression Retriever is developed, combining the document compressor and the retrieval mechanism. This retriever is key in obtaining relevant and concise recipe information, tailored to specific ingredient queries.


3.5 Recipe Generation and QA Pipeline

1. Retrieval-QA Chain
The RetrievalQA chain integrates the retrieval and compression functionalities. It is respon-sible for generating recipes in response to specific queries, considering user-specified constraints and preferences.

3. Query Processing
The system is designed to handle queries that specify particular ingredients and constraints. This functionality allows for the generation of customized recipes, adhering to user requirements and dietary preferences.

4 Experiments
The experimental setup is designed to explore and evaluate the performance of a recipe generation system comprising three key components: Recipe Search, Embedding and Retrieval, and Recipe Generation with GPT-4. The aim is to assess the effectiveness and creativity of the system in generating relevant and diverse recipes based on user-input ingredients. The experimental phases are outlined below:

1. Recipe Search:
BM25Okapi Model: The first phase involves querying the BM25Okapi model with a predefined list of ingredients to retrieve relevant
recipes. The BM25Okapi model is chosen for its efficiency in information retrieval tasks. Assessment of Relevance and Diversity: Following recipe retrieval, the relevance and diversity of the obtained recipes are assessed. Metrics such as relevance score and diversity index may be used to quantify the quality of the retrieved recipes.

2. Embedding and Retrieval:
OpenAIEmbeddings: Recipe steps are converted into embeddings using the OpenAIEmbeddings model. These embeddings serve as
numerical representations of the textual information in recipe steps. FAISS Retrieval: The embeddings are utilized to create a re-
triever using the FAISS library, enabling efficient similarity-based retrieval. This phase focuses on enhancing the precision and speed of recipe retrieval.

3. Recipe Generation with GPT-4:
GPT-4 Model: The GPT-4 model is employed to generate recipes based on the input ingredients. The generation process involves leveraging the contextual understanding and languag generation capabilities of GPT-4.

4. Comparative Analysis with GPT-4 vs. Rag-
Pipeline:
Rag-Pipeline Comparison: A comparative analysis is conducted between recipes generated by GPT-4 and those produced by the
RetrievalQA pipeline, specifically the Rag-Pipeline. Analyzing Differences: Differences in terms of ingredient use, recipe structure, and novelty are scrutinized to understand the strengths and weaknesses of each approach.

6. Ingredient Accuracy Assessment:
Deviation Analysis: A dedicated function is implemented to count extra ingredients present in the generated recipes compared to
the original input list. Frequency Calculation: The frequency of deviation from the originalingredient list is calculated, providing insights into how often the generated recipes introduce additional elements not specified in the input

5 Evaluation

1. Evaluation Metrics:
Given our limitations in evaluating openended generation, we concentrate on a more tangible aspect: analyzing the additional ingredients introduced by our recipe generator. Human preference modeling, constrained by budget and computational considerations, is set aside in favor of a more practical assessment that provides insights into the generator’s behavior concerning ingredient utilization.Therefore, we establish a unique metric considering the variance in the number of ingredients between the generated recipe and the originally provided ingredients. This metric produces a normalized representation of the disparity, and the average is computed across all samples for comprehensive evaluation.


2. A higher score indicates more deviation fromthe original list, implying the AI model adds, unexpected ingredients, which might not be ideal for users needing strict adherence to their

6 Conclusions

The study conducted on AI models in recipe generation and retrieval, using a combination of BM25Okapi, OpenAIEmbeddings and FAISS, and GPT-4, has provided valuable insights into the potential of AI in the culinary domain. The BM25Okapi model proved effective in sourcing recipes based on specific ingredients, offering a practical tool for home cooks and those with dietary restrictions. Meanwhile, the integration of OpenAIEmbeddings and FAISS showcased the AI’s capability in intelligently linking recipe stepswith ingredients, suggesting the possibility of more intuitive and user-centric recipe recommendation systems.
The use of GPT-4 for creative recipe generationwas a highlight of the study, demonstrating the model’s ability to craft unique recipes from given ingredients. This opens up exciting opportunities for personalized cooking guides and automated recipe creation. A comparative analysis between GPT-4 and the RetrievalQA pipeline revealed distinct strengths in each system, with variations in
ingredient fidelity, recipe structure, and innovation.
However, the study also noted challenges in maintaining ingredient accuracy, underscoring the need for further refinement in AI models for enhanced precision and relevance. In conclusion, this study has demonstrated that AI has significant potential in the culinary field, from assisting in recipe retrieval to creating novel recipes.
However, it also highlighted the need for further refinement in AI models to enhance accuracy and relevance. These findings pave the way for future research and development in AI-powered culinary tools, promising to revolutionize how we explore and experience food.
