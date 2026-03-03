# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMadantext(RPackage):
	"""Persian Text Mining Tool for Frequency Analysis, Statistical
Analysis, and Word Clouds

	This is an open-source software designed specifically for text mining in the Persian language. It allows users to examine word frequencies, download data for analysis, and generate word clouds. This tool is particularly useful for researchers and analysts working with Persian language data.
    This package mainly makes use of the 'PersianStemmer' (Safshekan, R., et al. (2019). <https://CRAN.R-project.org/package=PersianStemmer>),
    'udpipe' (Wijffels, J., et al. (2023). <https://CRAN.R-project.org/package=udpipe>),
    and 'shiny' (Chang, W., et al. (2023). <https://CRAN.R-project.org/package=shiny>) packages.
	"""
	
	cran = "MadanText" 

	version("0.1.0", md5="07d3fc79c68ac941e8840cd092c3844e")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-xlsx", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-stopwords", type=("build", "run"))
	depends_on("r-textminer", type=("build", "run"))
	depends_on("r-tidytext", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-udpipe", type=("build", "run"))
	depends_on("r-persianstemmer", type=("build", "run"))
	depends_on("r-shiny@1.8:", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
	depends_on("r-tm", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-hwordcloud", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-topicmodels", type=("build", "run"))
