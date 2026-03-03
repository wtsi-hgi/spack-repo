# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRarenmtests(RPackage):
	"""Ecological and Biogeographical Null Model Tests for Comparing
Rarefaction Curves

	Randomization tests for the statistical comparison of i = two or more individual-based, sample-based or coverage-based rarefaction curves. The ecological null hypothesis is that the i samples were all drawn randomly from a single assemblage, with (necessarily) a single underlying species abundance distribution. The biogeographic null hypothesis is that the i samples were all drawn from different assemblages that, nonetheless, share similar species richness and species abundance distributions. Functions are described in L. Cayuela, N.J. Gotelli & R.K. Colwell (2015) <doi:10.1890/14-1261.1>.
	"""
	
	cran = "rareNMtests" 

	version("1.2", md5="a8c1a5bc463fc65e1801dc7bb99eb1dc")

	depends_on("r-vegan", type=("build", "run"))
