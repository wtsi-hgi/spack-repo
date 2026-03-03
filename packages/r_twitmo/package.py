# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTwitmo(RPackage):
	"""Twitter Topic Modeling and Visualization for R

	Tailored for topic modeling with tweets and fit for visualization tasks in R.
    Collect, pre-process and analyze the contents of tweets using 
    LDA and structural topic models (STM). Comes with visualizing capabilities like tweet and hashtag maps 
    and built-in support for 'LDAvis'.
	"""
	
	homepage = "https://github.com/abuchmueller/Twitmo"
	cran = "Twitmo" 

	version("0.1.2", md5="db17e26d9589af30635d035cc1b54ee0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-stopwords", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rtweet", type=("build", "run"))
	depends_on("r-quanteda", type=("build", "run"))
	depends_on("r-quanteda-textstats", type=("build", "run"))
	depends_on("r-topicmodels", type=("build", "run"))
	depends_on("r-stm", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
	depends_on("r-ldavis", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-ldatuning", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-tm", type=("build", "run"))
