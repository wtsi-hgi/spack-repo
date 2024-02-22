# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFundiversity(RPackage):
	"""Easy Computation of Functional Diversity Indices

	Computes six functional diversity indices. These are namely,
  Functional Divergence (FDiv), Function Evenness (FEve), Functional Richness
  (FRic), Functional Richness intersections (FRic_intersect), Functional
  Dispersion (FDis), and Rao's entropy (Q) (reviewed in Villéger et al. 2008
  <doi:10.1890/07-1206.1>). Provides efficient, modular, and parallel functions
  to compute functional diversity indices
  (preprint: <doi:10.32942/osf.io/dg7hw>).
	"""
	
	homepage = "https://funecology.github.io/fundiversity/"
	cran = "fundiversity" 

	version("1.1.1", md5="2b40c15100b9e84c732af233b7bb6cf8")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-geometry", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
