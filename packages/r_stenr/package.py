# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStenr(RPackage):
	"""Standardization of Raw Discrete Questionnaire Scores

	An user-friendly framework to preprocess raw item
             scores of questionnaires into factors or scores and standardize
             them. Standardization can be made either by their normalization
             in representative sample, or by import of premade scoring table.
	"""
	
	homepage = "https://statismike.github.io/stenR/"
	cran = "stenR" 

	version("0.6.9", md5="5009d49fd6dc6c7f06ebff2787f42e51")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
