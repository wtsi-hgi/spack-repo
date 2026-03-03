# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTheopenair(RPackage):
	"""Integrate 'OpenAI' Large Language Models into Your 'R' Workflows

	Utilizing the 'OpenAI' API as the back end (<https://platform.openai.com/docs/api-reference>), 'TheOpenAIR' offers 'R' wrapper functions for the 'ChatGPT' endpoint and several high-level functions that enable the integration of 'ChatGPT' capabilities in diverse data-related tasks, such as data cleansing and automated analytics script generation.
	"""
	
	homepage = "http://openair-lib.org/"
	cran = "TheOpenAIR" 

	version("0.1.0", md5="b9dbb59722095768987e030126431919")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
