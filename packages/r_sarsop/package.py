# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSarsop(RPackage):
	"""Approximate POMDP Planning Software

	A toolkit for Partially Observed Markov Decision Processes (POMDP). Provides
    bindings to C++ libraries implementing the algorithm SARSOP (Successive Approximations
    of the Reachable Space under Optimal Policies) and described in Kurniawati et al (2008),
    <doi:10.15607/RSS.2008.IV.009>.  This package also provides a high-level interface
    for generating, solving and simulating POMDP problems and their solutions.
	"""
	
	homepage = "https://github.com/boettiger-lab/sarsop"
	cran = "sarsop" 

	version("0.6.14", md5="444db5d9d4d8648d1bf4577a11bdf841")

	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-processx", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
