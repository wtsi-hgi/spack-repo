# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsentiment(RPackage):
	"""Fetching Tweet Data for Sentiment Analysis

	Which uses Twitter APIs for the necessary data in sentiment analysis, acts as a middleware with the approved Twitter Application.
    A special access key is given to users who subscribe to the application with their Twitter account. With this special access key, the user defined keyword for sentiment analysis can be searched in twitter recent searches and results can be obtained( more information <https://github.com/hakkisabah/tsentiment> ).
    In addition, a service named tsentiment-services has been developed to provide all these operations ( for more information <https://github.com/hakkisabah/tsentiment-services> ).
    After the successful results obtained and in line with the permissions given by the user, the results of the analysis of the word cloud and bar graph saved in the user folder directory can be seen. In each analysis performed, the previous analysis visual result is deleted and this is the basic information you need to know as a practice rule.
    'tsentiment' package provides a free service that acts as a middleware for easy data extraction from Twitter, and in return, the user rate limit is reduced by 30 requests from the total limit and the remaining requests are used. These 30 requests are reserved for use in application analytics. For information about endpoints, you can refer to the limit information in the "GET search/tweets" row in the Endpoints column in the list at <https://developer.twitter.com/en/docs/twitter-api/v1/rate-limits>.
	"""
	
	homepage = "https://github.com/hakkisabah/tsentiment"
	cran = "tsentiment" 

	version("1.0.5", md5="4951bfbbac60ca62c3de6c140b91d3ac")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-wordcloud", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-syuzhet", type=("build", "run"))
	depends_on("r-tidytext", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
