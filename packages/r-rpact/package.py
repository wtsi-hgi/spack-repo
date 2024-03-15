# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpact(RPackage):
	"""Confirmatory Adaptive Clinical Trial Design and Analysis

	Design and analysis of confirmatory adaptive clinical trials with continuous, binary, and survival endpoints according to the methods described in the monograph by Wassmer and Brannath (2016) <doi:10.1007/978-3-319-32562-0>. This includes classical group sequential as well as multi-stage adaptive hypotheses tests that are based on the combination testing principle.
	"""
	
	homepage = "https://www.rpact.org"
	cran = "rpact" 

	version("3.5.1", md5="fa373636fe43b504eb8db2e21b8740f0")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-knitr@1.19:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
