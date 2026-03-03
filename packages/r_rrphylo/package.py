# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRrphylo(RPackage):
	"""Phylogenetic Ridge Regression Methods for Comparative Studies

	Functions for phylogenetic analysis (Castiglione et al., 2018 <doi:10.1111/2041-210X.12954>). The functions perform the estimation of phenotypic evolutionary rates, identification of phenotypic evolutionary rate shifts, quantification of direction and size of evolutionary change in multivariate traits, the computation of ontogenetic shape vectors and test for morphological convergence.
	"""
	
	cran = "RRphylo" 

	version("2.8.0", md5="0196c72a444f932041494ce27e46e2c5")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-emmeans@1.4.3:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-phytools", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
