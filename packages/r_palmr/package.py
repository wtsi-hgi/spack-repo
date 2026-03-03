# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPalmr(RPackage):
	"""Interface for 'Google Pathways Language Model 2 (PaLM 2)'

	'Google Pathways Language Model 2 (PaLM 2)' as a coding and writing assistant designed for 'R'. With a range of functions, including natural language processing and coding optimization, to assist 'R' developers in simplifying tedious coding tasks and content searching.
	"""
	
	homepage = "https://palmr.ly.gd.edu.kg/"
	cran = "PaLMr" 

	version("0.2.0", md5="48270e94767aaaf93b16744fe088c3c0")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
