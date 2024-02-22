# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNiaidmi(RPackage):
	"""Markov Model Multiple Imputation for NIAID OS

	The implementation of Markov Model Multiple Imputation
  with the application to COVID-19 scale, NIAID OS.
	"""
	
	cran = "niaidMI" 

	version("1.1.0", md5="94116423ac7828c2524b0a49293d5f78")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
