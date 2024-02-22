# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSentimentAi(RPackage):
	"""Simple Sentiment Analysis Using Deep Learning

	Sentiment Analysis via deep learning and gradient boosting models with a lot of the underlying hassle taken care of to make the process as simple as possible. 
  In addition to out-performing traditional, lexicon-based sentiment analysis (see <https://benwiseman.github.io/sentiment.ai/#Benchmarks>),
  it also allows the user to create embedding vectors for text which can be used in other analyses.
  GPU acceleration is supported on Windows and Linux.
	"""
	
	homepage = "https://benwiseman.github.io/sentiment.ai/"
	cran = "sentiment.ai" 

	version("0.1.1", md5="a9f7912357eb845df2857c25600e4aeb")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-data-table@1.12.8:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-reticulate@1.16:", type=("build", "run"))
	depends_on("r-roperators@1.2:", type=("build", "run"))
	depends_on("r-tensorflow@2.2:", type=("build", "run"))
	depends_on("r-tfhub@0.8:", type=("build", "run"))
	depends_on("r-xgboost", type=("build", "run"))
