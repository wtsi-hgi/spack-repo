# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRollama(RPackage):
	"""Communicate with 'Ollama'

	Wraps the 'Ollama' <https://ollama.ai> API, which can be used to 
    communicate with generative large language models locally.
	"""
	
	homepage = "https://jbgruber.github.io/rollama/"
	cran = "rollama" 

	version("0.0.2", md5="9578770a80ea47149e5b35715bf39129")

	depends_on("r-callr", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-prettyunits", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
