# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFhtest(RPackage):
	"""Tests for Right and Interval-Censored Survival Data Based on the
Fleming-Harrington Class

	Functions to compare two or more survival curves with:
             a) The Fleming-Harrington test for right-censored data based on permutations and on counting processes.
             b) An extension of the Fleming-Harrington test for interval-censored data based on a permutation distribution and on a score vector distribution.
	"""
	
	cran = "FHtest" 

	version("1.5.1", md5="7d60e8f0d045c6c53d28764d21d757a2")

	depends_on("r-interval", type=("build", "run"))
	depends_on("r-kmsurv", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-perm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
