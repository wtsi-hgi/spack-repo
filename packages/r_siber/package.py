# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSiber(RPackage):
	"""Stable Isotope Bayesian Ellipses in R

	Fits bi-variate ellipses to stable isotope data using Bayesian
    inference with the aim being to describe and compare their isotopic
    niche.
	"""
	
	cran = "SIBER" 

	version("2.1.9", md5="46c6a639433e317c2d8ea3afe83facf8")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-hdrcde", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-spatstat-utils", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("jags@4.1:", type=("build", "link", "run"))
