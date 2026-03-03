# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPh2bayes(RPackage):
	"""Bayesian Single-Arm Phase II Designs

	An implementation of Bayesian single-arm phase II design methods for binary outcome based on posterior
  probability (Thall and Simon (1994) <doi:10.2307/2533377>) and predictive probability (Lee and Liu (2008) <doi:10.1177/1740774508089279>).
	"""
	
	cran = "ph2bayes" 

	version("0.0.2", md5="42411b527b60adf2f94adcc5d541782e")

	depends_on("r-rcpp", type=("build", "run"))
