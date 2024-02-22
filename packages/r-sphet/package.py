# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSphet(RPackage):
	"""Estimation of Spatial Autoregressive Models with and without
Heteroskedastic Innovations

	Functions for fitting Cliff-Ord-type spatial autoregressive models with and without heteroskedastic innovations using Generalized Method of Moments estimation are provided. Some support is available for fitting spatial HAC models, and for fitting with non-spatial endogeneous variables using instrumental variables.
	"""
	
	homepage = "https://github.com/gpiras/sphet"
	cran = "sphet" 

	version("2.0", md5="efb32c9c5087b6f08fa497ed2a17cab2")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-spatialreg", type=("build", "run"))
	depends_on("r-spdep", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-spdata", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
