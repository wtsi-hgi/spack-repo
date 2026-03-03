# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPedsimulate(RPackage):
	"""Pedigree, Genetic Merit, Phenotype, and Genotype Simulation

	Simulate pedigree, genetic merits and phenotypes with random/non-random matings followed by random/non-random selection with different intensities and patterns in males and females. Genotypes can be simulated for a given pedigree, or an appended pedigree to an existing pedigree with genotypes.
   Mrode, R. A. (2005) <ISBN:9780851989969, 0851989969>;
   Nilforooshan, M.A. (2022) <doi:10.37496/rbz5120210131>.
	"""
	
	homepage = "https://github.com/nilforooshan/pedSimulate"
	cran = "pedSimulate" 

	version("1.4.3", md5="713b2eefe82c09ee5fc9b762d997c4a3")

