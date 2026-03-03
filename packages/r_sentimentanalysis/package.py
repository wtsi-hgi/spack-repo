# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSentimentanalysis(RPackage):
	"""Dictionary-Based Sentiment Analysis

	Performs a sentiment analysis of textual contents in R. This implementation
    utilizes various existing dictionaries, such as Harvard IV, or finance-specific 
    dictionaries. Furthermore, it can also create customized dictionaries. The latter 
    uses LASSO regularization as a statistical approach to select relevant terms based on 
    an exogenous response variable. 
	"""
	
	homepage = "https://github.com/sfeuerriegel/SentimentAnalysis"
	cran = "SentimentAnalysis" 

	version("1.3-5", md5="9796614f4de6bda206843d4805f8cd18")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-tm@0.6:", type=("build", "run"))
	depends_on("r-qdapdictionaries", type=("build", "run"))
	depends_on("r-ngramrr@0.1:", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-spikeslab@1.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
