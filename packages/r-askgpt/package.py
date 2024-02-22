# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAskgpt(RPackage):
	"""Asking GPT About R Stuff

	A chat package connecting to API endpoints by 'OpenAI' 
  (<https://platform.openai.com/>) to answer questions (about R).
	"""
	
	homepage = "https://github.com/JBGruber/askgpt"
	cran = "askgpt" 

	version("0.1.3", md5="24a13ee5ea52a05fa7d25b3b2acc8cac")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-callr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
