# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlma(RPackage):
	"""Multilevel Mediation Analysis

	Do multilevel mediation analysis with generalized additive multilevel models. The analysis method is described in Yu and Li (2020), "Third-Variable Effect Analysis with Multilevel Additive Models", PLoS ONE 15(10): e0241072.  
	"""
	
	homepage = "https://cran.r-project.org/package=mlma"
	cran = "mlma" 

	version("6.3-1", md5="240653a727c7bd9b6634d00ce7b11187")

	depends_on("r@2.14.1:", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-coxme", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
