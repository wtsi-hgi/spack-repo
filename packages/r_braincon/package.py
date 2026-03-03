# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBraincon(RPackage):
	"""Inference the Partial Correlations Based on Time Series Data

	A statistical tool to inference the multi-level partial correlations based on multi-subject time series data, especially for brain functional connectivity. It combines both individual and population level inference by using  the methods of Qiu and Zhou. (2021)<DOI: 10.1080/01621459.2021.1917417> and Genovese and Wasserman. (2006)<DOI: 10.1198/016214506000000339>. It realizes two reliable estimation methods of partial correlation coefficients, using scaled lasso and lasso. It can be used to estimate individual- or population-level partial correlations, identify nonzero ones, and find out unequal partial correlation coefficients between two populations.
	"""
	
	cran = "BrainCon" 

	version("0.3.0", md5="90f3e20fc71df0a0f69cb520af9e9792")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
