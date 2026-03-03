# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGillespiessa2(RPackage):
	"""Gillespie's Stochastic Simulation Algorithm for Impatient People

	A fast, scalable, and versatile framework for
    simulating large systems with Gillespie's Stochastic Simulation
    Algorithm ('SSA').  This package is the spiritual successor to the
    'GillespieSSA' package originally written by Mario Pineda-Krch.
    Benefits of this package include major speed improvements (>100x),
    easier to understand documentation, and many unit tests that try to
    ensure the package works as intended. Cannoodt and Saelens et al. (2021) 
    <doi:10.1038/s41467-021-24152-2>.
	"""
	
	homepage = "https://rcannood.github.io/GillespieSSA2/"
	cran = "GillespieSSA2" 

	version("0.3.0", md5="00b66f0bab5e9e55a19b884cdf0e6c99", url="https://cran.r-project.org/src/contrib/GillespieSSA2_0.3.0.tar.gz")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dynutils", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppxptrutils", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
