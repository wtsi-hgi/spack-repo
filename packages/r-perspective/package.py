# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPerspective(RPackage):
	"""Interface to the 'Perspective' API

	Interface to the 'Perspective' API, which can be found at the following URL: <https://github.com/conversationai/perspectiveapi#perspective-comment-analyzer-api>. 
    The 'Perspective' API uses machine learning models to score the perceived impact a comment might have on a conversation (i.e. TOXICITY, INFLAMMATORY, etc.).     
    'peRspective' provides access to the API and returns tidy data frames with results of the specified machine learning model(s).
	"""
	
	homepage = "https://favstats.github.io/peRspective/"
	cran = "peRspective" 

	version("0.1.1", md5="925f8fb7ad37719f06f3761565ea4023")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
