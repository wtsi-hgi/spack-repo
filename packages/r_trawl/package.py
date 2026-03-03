# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrawl(RPackage):
	"""Estimation and Simulation of Trawl Processes

	Contains R functions for simulating and estimating integer-valued trawl processes as 
    described in the article Veraart (2019),"Modeling, simulation and inference for
    multivariate time series of counts using trawl processes", Journal of Multivariate Analysis,
    169, pages 110-129,
    <doi:10.1016/j.jmva.2018.08.012> and for 
    simulating random vectors from the bivariate negative binomial and the bi- and trivariate 
    logarithmic series distributions.
	"""
	
	cran = "trawl" 

	version("0.2.2", md5="7a04a33e86034c37d02cd7040dcf83af")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-deoptim", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
	depends_on("r-runuran", type=("build", "run"))
	depends_on("r-squash", type=("build", "run"))
	depends_on("r-tsa", type=("build", "run"))
