# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLpda(RPackage):
	"""Linear Programming Discriminant Analysis

	Classification method obtained through linear programming.
    It is advantageous with respect to the classical developments when the distribution of the variables
    involved is unknown or when the number of variables is much greater than the number of individuals.
    LPDA method is published in Nueda, et al. (2022) "LPDA: A new classification method based on linear programming".
    <doi:10.1371/journal.pone.0270403>.
	"""
	
	cran = "lpda" 

	version("1.0.1", md5="212ebd2c0dc9e664fc67cab3bf0d373b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rglpk", type=("build", "run"))
