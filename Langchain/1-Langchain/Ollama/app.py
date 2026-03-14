{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "2525bed2",
   "metadata": {},
   "source": [
    "#### Simple Gen AI APP Using Langchain"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "58c43b80",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import os\n",
    "from dotenv import load_dotenv\n",
    "\n",
    "from langchain_community.llms import Ollama\n",
    "import streamlit as st\n",
    "from langchain_core.prompts import ChatPromptTemplate\n",
    "from langchain_core.output_parsers import StrOutputParser\n",
    "\n",
    "load_dotenv()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "6169d4fa",
   "metadata": {},
   "outputs": [],
   "source": [
    "## Langsmith Tracking\n",
    "os.environ[\"LANGCHAIN_API_KEY\"]=os.getenv(\"LANGCHAIN_API_KEY\")\n",
    "os.environ[\"LANGCHAIN_TRACING_V2\"]=\"true\"\n",
    "os.environ[\"LANGCHAIN_PROJECT\"]=os.getenv(\"LANGCHAIN_PROJECT\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "13f053b0",
   "metadata": {},
   "outputs": [],
   "source": [
    "## Prompt Template\n",
    "prompt=ChatPromptTemplate.from_messages(\n",
    "    [\n",
    "        (\"system\",\"You are a helpful assistant. Please respond to the question asked\"),\n",
    "        (\"user\",\"Question:{question}\")\n",
    "    ]\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "f344b86b",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2026-03-08 01:02:38.631 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-08 01:02:41.425 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run c:\\Users\\VikashMahato\\Udemy Learning\\Langchain\\venv\\lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2026-03-08 01:02:41.429 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-08 01:02:41.441 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-08 01:02:41.446 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-08 01:02:41.450 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-08 01:02:41.451 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-08 01:02:41.460 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-08 01:02:41.462 Session state does not function when running a script without `streamlit run`\n",
      "2026-03-08 01:02:41.471 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-08 01:02:41.473 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-08 01:02:41.475 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "##  streamlit framework\n",
    "st.title(\"Langchain Demo With Gemma Model\")\n",
    "input_text=st.text_input(\"What question you have in mind?\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "5c175d87",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\VikashMahato\\AppData\\Local\\Temp\\ipykernel_31936\\1381307575.py:2: LangChainDeprecationWarning: The class `Ollama` was deprecated in LangChain 0.3.1 and will be removed in 1.0.0. An updated version of the class exists in the `langchain-ollama package and should be used instead. To use it run `pip install -U `langchain-ollama` and import as `from `langchain_ollama import OllamaLLM``.\n",
      "  llm=Ollama(model=\"gemma:2b\")\n"
     ]
    }
   ],
   "source": [
    "\n",
    "## Ollama Llama2 model\n",
    "llm=Ollama(model=\"gemma:2b\")\n",
    "output_parser=StrOutputParser()\n",
    "chain=prompt|llm|output_parser\n",
    "\n",
    "if input_text:\n",
    "    st.write(chain.invoke({\"question\":input_text}))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c33e0164",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "venv",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.19"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
