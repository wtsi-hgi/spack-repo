# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSim1000g(RPackage):
	"""Genotype Simulations for Rare or Common Variants Using
Haplotypes from 1000 Genomes

	Generates realistic simulated genetic data in families or unrelated individuals.
	"""
	
	cran = "sim1000G" 

	version("1.40", md5="c561ca6fe4331eede6fe4d519f680654")

	depends_on("r@2.15.2:", type=("build", "run"))
	depends_on("r-hapsim", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
