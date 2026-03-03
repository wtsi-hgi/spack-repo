# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCorehunter(RPackage):
	"""Multi-Purpose Core Subset Selection

	Core Hunter is a tool to sample diverse, representative subsets from large germplasm
    collections, with minimum redundancy. Such so-called core collections have applications in plant
    breeding and genetic resource management in general. Core Hunter can construct cores based on
    genetic marker data, phenotypic traits or precomputed distance matrices, optimizing one of many
    provided evaluation measures depending on the precise purpose of the core (e.g. high diversity,
    representativeness, or allelic richness). In addition, multiple measures can be simultaneously
    optimized as part of a weighted index to bring the different perspectives closer together.
    The Core Hunter library is implemented in Java 8 as an open source project (see
    <http://www.corehunter.org>).
	"""
	
	cran = "corehunter" 

	version("3.2.3", md5="2ff0bdd301898de9af5572329ec245ad")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-rjava@0.9.8:", type=("build", "run"))
	depends_on("r-naturalsort@0.1.2:", type=("build", "run"))
	depends_on("openjdk@8:", type=("build", "link", "run"))
