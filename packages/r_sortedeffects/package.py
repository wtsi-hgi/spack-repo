# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSortedeffects(RPackage):
	"""Estimation and Inference Methods for Sorted Causal Effects and
Classification Analysis

	Implements the estimation and inference methods for sorted causal effects and 
    classification analysis as in Chernozhukov, Fernandez-Val and Luo (2018) <doi:10.3982/ECTA14415>.
	"""
	
	homepage = "https://github.com/shuowencs/SortedEffects"
	cran = "SortedEffects" 

	version("1.7.0", md5="e7fc0f5aa7734cac44e5224d1e248aaa")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-sparsem", type=("build", "run"))
