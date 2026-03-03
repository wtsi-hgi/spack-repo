# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSigr(RPackage):
	"""Succinct and Correct Statistical Summaries for Reports

	Succinctly and correctly format statistical summaries of
    various models and tests (F-test, Chi-Sq-test, Fisher-test, T-test, and rank-significance). 
    This package also includes empirical tests, such as Monte Carlo and bootstrap distribution estimates.
	"""
	
	homepage = "https://github.com/WinVector/sigr/"
	cran = "sigr" 

	version("1.1.5", md5="c5bf13538dae9d6705a26303374e0a3e")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-wrapr@2.0.9:", type=("build", "run"))
