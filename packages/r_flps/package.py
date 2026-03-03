# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlps(RPackage):
	"""Fully-Latent Principal Stratification

	Simulation and analysis of Fully-Latent Principal Stratification (FLPS) with measurement models. Sales & Pane (2019). <doi:10.1214/18-AOAS1196>. This package is supported by the Institute of Education Sciences, U.S. Department of Education, through Grant R305D210036.
	"""
	
	homepage = "https://sooyongl.github.io/flps/"
	cran = "flps" 

	version("1.0.0", md5="2c201ac22b6d821fe7d07ba4fc9f02a3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rstan", type=("build", "run"))
	depends_on("r-rcpp@1.0.8.3:", type=("build", "run"))
	depends_on("r-mirt", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
