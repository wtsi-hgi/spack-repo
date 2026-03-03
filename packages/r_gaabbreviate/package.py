# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGaabbreviate(RPackage):
	"""Abbreviating Items Measures using Genetic Algorithms

	Scale abbreviation using Genetic Algorithms that maximally capture the variance in the original data.
	"""
	
	cran = "GAabbreviate" 

	version("1.3", md5="d396b5b3bdaedd43d10320cc4467d821")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-ga@3:", type=("build", "run"))
	depends_on("r-psych@1.4.3:", type=("build", "run"))
