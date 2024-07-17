#!/bin/bash

# Clone the repos
git clone https://github.com/AI4Bharat/indicTrans.git
cd indicTrans

# Clone requirements repositories
git clone https://github.com/anoopkunchukuttan/indic_nlp_library.git
git clone https://github.com/anoopkunchukuttan/indic_nlp_resources.git
git clone https://github.com/rsennrich/subword-nmt.git
cd ..

# Install requirements
pip install sacremoses pandas mock sacrebleu tensorboardX pyarrow indic-nlp-library
pip install mosestokenizer subword-nmt

# Install fairseq from source
git clone https://github.com/pytorch/fairseq.git
cd fairseq
pip install ./
pip install xformers
cd ..

# Download the en2indic model
wget https://ai4b-public-nlu-nlg.objectstore.e2enetworks.net/en2indic.zip
unzip en2indic.zip

# Add fairseq folder to python path
export PYTHONPATH=$PYTHONPATH:$(pwd)/fairseq
