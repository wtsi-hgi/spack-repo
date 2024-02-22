# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBifactorindicescalculator(RPackage):
	"""Bifactor Indices Calculator

	The calculator computes bifactor indices such as explained common variance (ECV), hierarchical Omega (OmegaH), percentage of uncontaminated correlations (PUC), item explained common variance (I-ECV), and more. This package is an R version of the 'Excel' based 'Bifactor Indices Calculator' (Dueber, 2017)  <doi:10.13023/edp.tool.01> with added convenience features for directly utilizing output from several programs that can fit confirmatory factor analysis or item response models.
	"""
	
	homepage = "https://github.com/ddueber/BifactorIndicesCalculator"
	cran = "BifactorIndicesCalculator" 

	version("0.2.2", md5="83195fd27678630bd4886dff769e5992")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-mirt", type=("build", "run"))
	depends_on("r-mplusautomation", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
