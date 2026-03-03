# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatsurv(RPackage):
	"""Bayesian Spatial Survival Analysis with Parametric Proportional
Hazards Models

	Bayesian inference for parametric proportional hazards spatial
    survival models; flexible spatial survival models. See Benjamin M. Taylor, Barry S. Rowlingson (2017) <doi:10.18637/jss.v077.i04>.
	"""
	
	cran = "spatsurv" 

	version("2.0-1", md5="0eb51373d0dea01692f00b2a05b48c8e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-spatstat-explore", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-spatstat-random", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
