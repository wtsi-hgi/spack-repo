# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExdqlm(RPackage):
	"""Extended Dynamic Quantile Linear Models

	Routines for Bayesian estimation and analysis of dynamic quantile linear models utilizing the extended asymmetric Laplace error distribution, also known as extended dynamic quantile linear models (exDQLM) described in Barata et al (2020) <doi:10.1214/21-AOAS1497>. 
	"""
	
	cran = "exdqlm" 

	version("0.1.3", md5="2520898f91f8017c20aec24342e0adc9")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dlm", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-tictoc", type=("build", "run"))
	depends_on("r-magic", type=("build", "run"))
	depends_on("r-crch", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-hyperbolicdist", type=("build", "run"))
	depends_on("r-generalizedhyperbolic", type=("build", "run"))
	depends_on("r-brms", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-laplacesdemon", type=("build", "run"))
