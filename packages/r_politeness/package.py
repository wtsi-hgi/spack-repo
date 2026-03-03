# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPoliteness(RPackage):
	"""Detecting Politeness Features in Text

	Detecting markers of politeness in English natural language. This package allows researchers to easily visualize and quantify politeness between groups of documents. This package combines prior research on the linguistic markers of politeness. We thank the Spencer Foundation, the Hewlett Foundation, and Harvard's Institute for Quantitative Social Science for support.
	"""
	
	cran = "politeness" 

	version("0.9.3", md5="47a15f6399bc3f498b37ded946908f75")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-tm", type=("build", "run"))
	depends_on("r-quanteda", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-spacyr", type=("build", "run"))
	depends_on("r-textir", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
