# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHspm(RPackage):
	"""Heterogeneous Spatial Models

	Spatial heterogeneity can be specified in various ways. 'hspm' is an ambitious project that aims at implementing various methodologies to control for heterogeneity in spatial models. The current version of 'hspm' deals with spatial and (non-spatial) regimes models. In particular, the package allows to estimate a general spatial regimes model with additional endogenous variables, specified in terms of a spatial lag of the dependent variable, the spatially lagged regressors, and, potentially, a spatially autocorrelated error term. Spatial regime models are estimated by instrumental variables and generalized methods of moments (see Arraiz et al., (2010) <doi:10.1111/j.1467-9787.2009.00618.x>, Bivand and Piras, (2015) <doi:10.18637/jss.v063.i18>, Drukker et al., (2013) <doi:10.1080/07474938.2013.741020>, Kelejian and Prucha, (2010) <doi:10.1016/j.jeconom.2009.10.025>).
	"""
	
	homepage = "https://github.com/gpiras/hspm"
	cran = "hspm" 

	version("1.1", md5="e863dfc95790adacf88527c65a129967")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-sphet", type=("build", "run"))
	depends_on("r-spdep", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
