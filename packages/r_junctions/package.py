# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJunctions(RPackage):
	"""The Breakdown of Genomic Ancestry Blocks in Hybrid Lineages

	Individual based simulations of hybridizing populations,
    where the accumulation of junctions is tracked. Furthermore,
    mathematical equations are provided to verify simulation outcomes.
    Both simulations and mathematical equations are based on Janzen
    (2018, <doi:10.1101/058107>) and Janzen (2020,
    <doi:10.1101/2020.09.10.292441>).
	"""
	
	homepage = "https//github.com/thijsjanzen/junctions"
	cran = "junctions" 

	version("2.1.0", md5="4300657c53620d3bdd34b32b7d027b10")

	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
