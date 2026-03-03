# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClikcorr(RPackage):
	"""Censoring Data and Likelihood-Based Correlation Estimation

	A profile likelihood based method of estimation and inference on the correlation coefficient of bivariate data with different types of censoring and missingness.
	"""
	
	cran = "clikcorr" 

	version("1.0", md5="7022e88964d558891092fe9738bdaee1")

	depends_on("r-mvtnorm", type=("build", "run"))
