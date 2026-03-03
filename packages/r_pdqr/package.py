# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPdqr(RPackage):
	"""Work with Custom Distribution Functions

	Create, transform, and summarize custom random
    variables with distribution functions (analogues of 'p*()', 'd*()',
    'q*()', and 'r*()' functions from base R). Two types of distributions
    are supported: "discrete" (random variable has finite number of output
    values) and "continuous" (infinite number of values in the form of
    continuous random variable). Functions for distribution
    transformations and summaries are available. Implemented approaches
    often emphasize approximate and numerical solutions: all distributions
    assume finite support and finite values of density function; some
    methods implemented with simulation techniques.
	"""
	
	homepage = "https://github.com/echasnovski/pdqr"
	cran = "pdqr" 

	version("0.3.1", md5="5b3a334dce39ed17aed565ab1d800441")

	depends_on("r@3.3:", type=("build", "run"))
