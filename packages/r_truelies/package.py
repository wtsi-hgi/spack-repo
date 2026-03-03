# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTruelies(RPackage):
	"""Bayesian Methods to Estimate the Proportion of Liars in Coin
Flip Experiments

	Implements Bayesian methods, described in
    Hugh-Jones (2019) <doi:10.1007/s40881-019-00069-x>, for estimating the
    proportion of liars in coin flip-style experiments, where subjects
    report a random outcome and are paid for reporting a "good" outcome.
	"""
	
	homepage = "https://github.com/hughjonesd/truelies"
	cran = "truelies" 

	version("0.2.0", md5="325d4154bc14d8791f73ed837abe4b36")

	depends_on("r-hdrcde", type=("build", "run"))
