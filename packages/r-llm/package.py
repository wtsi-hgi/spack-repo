# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLlm(RPackage):
	"""Logit Leaf Model Classifier for Binary Classification

	Fits the Logit Leaf Model, makes predictions and visualizes the output. (De Caigny et al., (2018) <DOI:10.1016/j.ejor.2018.02.009>).
	"""
	
	cran = "LLM" 

	version("1.1.0", md5="3e38c868f0f3e6b09935916d8513e969")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-partykit", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rweka", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
	depends_on("r-reghelper", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
