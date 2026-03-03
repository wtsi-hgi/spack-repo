# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPplasso(RPackage):
	"""Prognostic Predictive Lasso for Biomarker Selection

	We provide new tools for the identification of prognostic and predictive biomarkers. For further details we refer the reader to the paper: Zhu et al. Identification of prognostic and predictive biomarkers in high-dimensional data with PPLasso. BMC Bioinformatics. 2023 Jan 23;24(1):25.
	"""
	
	cran = "PPLasso" 

	version("2.0", md5="541bec2a4acddb5ad523fbf402e759fe")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genlasso", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cvcovest", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
