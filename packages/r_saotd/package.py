# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSaotd(RPackage):
	"""Sentiment Analysis of Twitter Data

	This analytic is an in initial foray into sentiment analysis.  
    This analytic will allow a user to access the Twitter API (once they create 
    their own developer account), ingest tweets of their interest, clean / tidy 
    data, perform topic modeling if interested, compute sentiment scores 
    utilizing the Bing Lexicon, and output visualizations.
	"""
	
	homepage = "https://github.com/evan-l-munson/saotd"
	cran = "saotd" 

	version("0.3.1", md5="b7854b8f6ce5b6bc8950a3a74bbbda81")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-widyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidytext", type=("build", "run"))
	depends_on("r-rtweet", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggraph", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ldatuning", type=("build", "run"))
	depends_on("r-topicmodels", type=("build", "run"))
	depends_on("gsl@2.4:", type=("build", "link", "run"))
	depends_on("mpfr@4.0.0:", type=("build", "link", "run"))
	depends_on("udunits@2:", type=("build", "link", "run"))
