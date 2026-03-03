# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuest(RPackage):
	"""Prepare Questionnaire Data for Analysis

	Offers a suite of functions to prepare questionnaire data for analysis (perhaps other types of data as well). By data preparation, I mean data analytic tasks to get your raw data ready for statistical modeling (e.g., regression). There are functions to investigate missing data, reshape data, validate responses, recode variables, score questionnaires, center variables, aggregate by groups, shift scores (i.e., leads or lags), etc. It provides functions for both single level and multilevel (i.e., grouped) data. With a few exceptions (e.g., ncases()), functions without an "s" at the end of their primary word (e.g., center_by()) act on atomic vectors, while functions with an "s" at the end of their primary word (e.g., centers_by()) act on multiple columns of a data.frame.
	"""
	
	cran = "quest" 

	version("0.2.0", md5="2b1a69e1d9ba5b59b7573ea365dca446")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-str2str", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-mbess", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-multilevel", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
