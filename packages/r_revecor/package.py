# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRevecor(RPackage):
	"""Reverse Ecology Analysis on Microbiome

	An implementation of the reverse ecology framework. Reverse ecology
    refers to the use of genomics to study ecology with no a priori assumptions
    about the organism(s) under consideration, linking organisms to their
    environment. It allows researchers to reconstruct the metabolic networks and
    study the ecology of poorly characterized microbial species from their
    genomic information, and has substantial potentials for microbial community
    ecological analysis.
	"""
	
	cran = "RevEcoR" 

	version("0.99.3", md5="c55d170cde2cc758787ceabf38b479ec")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
