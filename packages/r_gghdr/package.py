# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGghdr(RPackage):
	"""Visualisation of Highest Density Regions in 'ggplot2'

	Provides 'ggplot2' framework for visualising Highest Density Regions (HDR) 
    <doi:10.1080/00031305.1996.10474359>. This work is based on
    the package 'hdrcde'<https://pkg.robjhyndman.com/hdrcde/> and 
    displays highest density regions in 'ggplot2' for one and two dimensions and
    univariate densities conditional on one covariate.
	"""
	
	homepage = "https://github.com/Sayani07/gghdr"
	cran = "gghdr" 

	version("0.2.0", md5="dee1ae2698616d57201e10ae2168b75d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-hdrcde", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-farver", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
