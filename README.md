# NLP Medical Diagnosis Classifier
AAI-501 Team 3 Final Project

## Overview

The primary objective of this project is to devise the backend model that will drive the self-diagnostic chat service. Essential to this endeavor is the development of a model capable of analyzing a patient's symptoms described in natural language and subsequently predicting the correct diagnosis with a minimum weighted F1 score and accuracy of 0.9. Moreover, it is imperative to construct an end-to-end pipeline that stands out not only for its computational efficiency but also its alignment with the latency prerequisites of an interactive chat service. On average, the system should execute predictions in under one second.

## Approach

The team aimed to identify the optimal technical approach for the project by designing experiments that assessed various text classification methods for performance and efficiency. Traditional ML algorithms, such as Naive Bayes, can be highly effective in solving text classification problems (HaCohen-Kerner et al., 2020).  This can be particularly effective when coupled with text preprocessing techniques such as stop word removal, punctuation removal and other similar techniques (HaCohen-Kerner et al., 2020).  Given the computational efficiency of these algorithms, the Naive Bayes method was selected for the initial experiment.
Contextualized word embeddings are another technique that perform well as part of a text classification solution (Raj et al., 2022). Embedding algorithms, such as Embeddings from Language Models (ELMo), are pre-trained on extensive text corpora, and when integrated with a neural network, yield highly precise text classification models (Raj et al., 2022). This methodology serves as the foundation for the second experiment.
In summary, two primary experiments were executed to advance our understanding of text classification. The first experiment involved training a Multinomial Naive Bayes Classifier (NBC) using traditional word embeddings, commonly referred to as vectorization. The second experiment focused on the deployment of a deep neural network classifier, harnessing the capabilities of ELMo contextual word embeddings. Notably, for both experimental paradigms, various text preprocessing techniques were applied, which are elaborated upon in the subsequent sections. 

