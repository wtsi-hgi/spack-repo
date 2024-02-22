# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimplybee(RPackage):
	"""'AlphaSimR' Extension for Simulating Honeybee Populations and
Breeding Programmes

	An extension of the 'AlphaSimR' package
  (<https://cran.r-project.org/package=AlphaSimR>) for stochastic simulations of
  honeybee populations and breeding programmes. 'SIMplyBee' enables simulation of
  individual bees that form a colony, which includes a queen, fathers (drones
  the queen mated with), virgin queens, workers, and drones. Multiple colony can
  be merged into a population of colonies, such as an apiary or a whole country
  of colonies. Functions enable operations on castes, colony, or colonies, to
  ease 'R' scripting of whole populations. All 'AlphaSimR' functionality with
  respect to genomes and genetic and phenotype values is available and further
  extended for honeybees, including haplo-diploidy, complementary sex determiner
  locus, colony events (swarming, supersedure, etc.), and colony phenotype values.
	"""
	
	homepage = "https://github.com/HighlanderLab/SIMplyBee"
	cran = "SIMplyBee" 

	version("0.3.0", md5="3cfa9f08917b207784871758ca28ef4a")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-alphasimr@1.3.2:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-extradistr@1.9.1:", type=("build", "run"))
