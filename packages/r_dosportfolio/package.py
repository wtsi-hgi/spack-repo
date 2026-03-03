# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDosportfolio(RPackage):
	"""Dynamic Optimal Shrinkage Portfolio

	
  Constructs dynamic optimal shrinkage estimators for the weights of the global 
  minimum variance portfolio which are reconstructed at given reallocation 
  points as derived in Bodnar, Parolya, and Thorsén (2021) (<arXiv:2106.02131>).
  Two dynamic shrinkage estimators are available in this package. One using 
  overlapping samples while the other use nonoverlapping samples.
	"""
	
	homepage = "https://github.com/Statistics-In-Portfolio-Theory/DOSportfolio"
	cran = "DOSPortfolio" 

	version("0.1.0", md5="4df4a8bdd06ecbb8e5d6ffc616f939aa")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rdpack@0.7:", type=("build", "run"))
