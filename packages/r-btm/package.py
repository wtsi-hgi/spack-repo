# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBtm(RPackage):
	"""Biterm Topic Models for Short Text

	Biterm Topic Models find topics in collections of short texts. 
    It is a word co-occurrence based topic model that learns topics by modeling word-word co-occurrences patterns which are called biterms.
    This in contrast to traditional topic models like Latent Dirichlet Allocation and Probabilistic Latent Semantic Analysis 
    which are word-document co-occurrence topic models.
    A biterm consists of two words co-occurring in the same short text window.  
    This context window can for example be a twitter message, a short answer on a survey, a sentence of a text or a document identifier. 
    The techniques are explained in detail in the paper 'A Biterm Topic Model For Short Text' by Xiaohui Yan, Jiafeng Guo, Yanyan Lan, Xueqi Cheng (2013) <https://github.com/xiaohuiyan/xiaohuiyan.github.io/blob/master/paper/BTM-WWW13.pdf>.
	"""
	
	homepage = "https://github.com/bnosac/BTM"
	cran = "BTM" 

	version("0.3.7", md5="e121e81a1c7b609467e1f11b2c5c21c0")

	depends_on("r-rcpp", type=("build", "run"))
