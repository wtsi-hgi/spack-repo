# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBlatent(RPackage):
	"""Bayesian Latent Variable Models

	Estimation of latent variable models using Bayesian methods. Currently estimates the loglinear cognitive diagnosis model of Henson, Templin, and Willse (2009) <doi:10.1007/s11336-008-9089-5>.
	"""
	
	cran = "blatent" 

	version("0.1.2", md5="9142f800afaeb1f3757dc2238cb299c3")

	depends_on("r-coda", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
	depends_on("r@3:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
