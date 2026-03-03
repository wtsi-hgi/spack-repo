# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFracture(RPackage):
	"""Convert Decimals to Fractions

	Provides functions for converting decimals to a
    matrix of numerators and denominators or a character vector of
    fractions.  Supports mixed or improper fractions, finding common
    denominators for vectors of fractions, limiting denominators to powers
    of ten, and limiting denominators to a maximum value.  Also includes
    helper functions for finding the least common multiple and greatest
    common divisor for a vector of integers.  Implemented using C++ for
    maximum speed.
	"""
	
	homepage = "https://fracture.rossellhayes.com/"
	cran = "fracture" 

	version("0.2.1", md5="dd01156732ef235301c99a6680846bf6")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
