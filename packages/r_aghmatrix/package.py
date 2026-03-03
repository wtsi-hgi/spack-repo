# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAghmatrix(RPackage):
	"""Relationship Matrices for Diploid and Autopolyploid Species

	Computation of A (pedigree), G (genomic-base), and H (A corrected
    by G) relationship matrices for diploid and autopolyploid species. Several methods
    are implemented considering additive and non-additive models.
	"""
	
	homepage = "https://github.com/rramadeu/AGHmatrix"
	cran = "AGHmatrix" 

	version("2.1.4", md5="801d547029b006831fd3ae0be45f4ce9")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-matrix@1.2.7.1:", type=("build", "run"))
	depends_on("r-zoo@1.8.6:", type=("build", "run"))
