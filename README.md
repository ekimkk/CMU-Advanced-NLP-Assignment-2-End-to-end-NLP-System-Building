# Advanced NLP Assignment 2: End-to-end NLP System Building

## Project Description
We built a end-to-end NLP System with RoBERTa, T5 and T5+Mistral. RoBERTa outperforms T5 and T5+Mistral in pinpointing precise answer spans. Although generative models like T5 and Mistral demonstrated their strength in providing more comprehensive information for high-level queries, the flexibility in generating more elaborate responses come with a trade-off: longer results and less accurate information. The remaining challenge that RoBERTa is faced with would be synthesizing information from multiple sources and reasoning over implicit knowledge.

## Getting Started
### Dependencies

Before running this project, you must install the required dependencies. This project's dependencies are listed in the `requirements.txt` file. To install them, run the following command:

```bash
pip install -r requirements.txt
```

### Installing and Executing
- Clone this repository to your local machine using git clone <repo-url>.
- Navigate to the cloned directory.
- Install the project dependencies using the command above.
- Proceed with the rest of the installation steps as described.

## File Descriptions
- Web Script Code: Source code for raw data extraction used in the project.
- data: Directory for training and test data of annotated Q&A pairs.
- system_outputs: Contains output data (answers) from three models.
- Mistral_Model.ipynb: Jupyter notebook for the Mistral model development.
- Model_Evaluation.ipynb: Jupyter notebook for evaluating the models.
- Roberta_Model.ipynb: Jupyter notebook for the Roberta model development.
- T5_Model.ipynb: Jupyter notebook for the T5 model development.
- reference.zip: A compressed file containing reference materials or datasets.

## Authors
- Ella Liang (jinqiul)
- Ellen Song (yuhans2)
- Alicia Wang (chenqiw)

## License
This project is licensed under the GNU General Public License v2.0 and Apache License v2.0- see the LICENSE folder for details.
