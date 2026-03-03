# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RElnnpairedcov(RPackage):
	"""Model-Based Gene Selection for Paired Data

	Model-based clustering for paired data based on the regression of a mixture of Bayesian hierarchical models on covariates. Zhang et al. (2023) <doi:10.1186/s12859-023-05556-x>.                      
	"""
	
	cran = "eLNNpairedCov" 

	version("0.3.2", md5="7a1f9df8d5b25e7738e34ac1c441e5e9")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
