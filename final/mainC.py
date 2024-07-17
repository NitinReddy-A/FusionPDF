## clone the repo for running evaluation
#!git clone https://github.com/AI4Bharat/indicTrans.git
#%cd indicTrans
## clone requirements repositories
#!git clone https://github.com/anoopkunchukuttan/indic_nlp_library.git
#!git clone https://github.com/anoopkunchukuttan/indic_nlp_resources.git
#!git clone https://github.com/rsennrich/subword-nmt.git
#%cd ..
## Install requirements
#!pip install sacremoses pandas mock sacrebleu tensorboardX pyarrow indic-nlp-library
#!pip install mosestokenizer subword-nmt
## Install fairseq from source
#!git clone https://github.com/pytorch/fairseq.git
#%cd fairseq
## xformers
#!pip install ./
#! pip install xformers
#%cd ..
## download the en2indic model
#!wget https://ai4b-public-nlu-nlg.objectstore.e2enetworks.net/en2indic.zip
#!unzip en2indic.zip
#%cd indicTrans
# add fairseq folder to python path
import os
#os.environ['PYTHONPATH'] += ":/content/fairseq/"
# sanity check to see if fairseq is installed
from fairseq import checkpoint_utils, distributed_utils, options, tasks, utils
from indicTrans.inference.engine import Model
en2indic_model = Model(expdir='../en-indic')