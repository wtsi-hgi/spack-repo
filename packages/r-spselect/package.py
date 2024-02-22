# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpselect(RPackage):
	"""Selecting Spatial Scale of Covariates in Regression Models

	Fits spatial scale (SS) forward stepwise regression, SS incremental forward stagewise regression, SS least angle regression (LARS), and SS lasso models.  All area-level covariates are considered at all available scales to enter a model, but the SS algorithms are constrained to select each area-level covariate at a single spatial scale.
	"""
	
	cran = "spselect" 

	version("0.0.1", md5="8b1e6a52eec4a324684c98aed1671866")

	depends_on("r-tester", type=("build", "run"))
	depends_on("r-magic", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
