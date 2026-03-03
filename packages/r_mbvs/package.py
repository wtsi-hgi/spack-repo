# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMbvs(RPackage):
	"""Bayesian Variable Selection Methods for Multivariate Data

	Bayesian variable selection methods for data with multivariate responses and multiple covariates. The package contains implementations of multivariate Bayesian variable selection methods for continuous data (Lee et al., Biometrics, 2017 <doi:10.1111/biom.12557>) and zero-inflated count data (Lee et al., Biostatistics, 2020 <doi:10.1093/biostatistics/kxy067>).
	"""
	
	cran = "mBvs" 

	version("1.6", md5="090c89bee861f843f65538780e538eb3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("gsl", type=("build", "link", "run"))
