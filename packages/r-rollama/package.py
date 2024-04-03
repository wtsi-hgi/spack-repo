# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRollama(RPackage):
	"""Communicate with 'Ollama'

	Wraps the 'Ollama' <https://ollama.com> API, which can be used to 
    communicate with generative large language models locally.
	"""
	
	homepage = "https://jbgruber.github.io/rollama/"
	cran = "rollama" 

	version("0.0.3", md5="29c77b8d63f5af1a37023ac3b4648446")

	depends_on("r-callr", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-prettyunits", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
