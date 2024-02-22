# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTexter(RPackage):
	"""An Easy Text and Sentiment Analysis Library

	Implement text and sentiment analysis with 'texter'. 
             Generate sentiment scores on text data and also visualize sentiments.
             'texter' allows you to quickly generate insights on your data.
             It includes support for lexicons such as 'NRC' and 'Bing'.
	"""
	
	homepage = "https://github.com/simmieyungie/texter"
	cran = "texter" 

	version("0.1.9", md5="ea66fde49747a9435496537cff1e892d")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stopwords", type=("build", "run"))
	depends_on("r-textdata", type=("build", "run"))
	depends_on("r-tidytext", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
