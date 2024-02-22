# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSentencepiece(RPackage):
	"""Text Tokenization using Byte Pair Encoding and Unigram Modelling

	Unsupervised text tokenizer allowing to perform byte pair encoding and unigram modelling. 
    Wraps the 'sentencepiece' library <https://github.com/google/sentencepiece> which provides a language independent tokenizer to split text in words and smaller subword units. 
    The techniques are explained in the paper "SentencePiece: A simple and language independent subword tokenizer and detokenizer for Neural Text Processing" by Taku Kudo and John Richardson (2018) <doi:10.18653/v1/D18-2012>.
    Provides as well straightforward access to pretrained byte pair encoding models and subword embeddings trained on Wikipedia using 'word2vec', 
    as described in "BPEmb: Tokenization-free Pre-trained Subword Embeddings in 275 Languages" by Benjamin Heinzerling and Michael Strube (2018) <http://www.lrec-conf.org/proceedings/lrec2018/pdf/1049.pdf>.
	"""
	
	homepage = "https://github.com/bnosac/sentencepiece"
	cran = "sentencepiece" 

	version("0.2.3", md5="13e8765e019f0f7b2b1ef1433fa5ddf9")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
