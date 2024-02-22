# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQtl2fst(RPackage):
	"""Database Storage of Genotype Probabilities for QTL Mapping

	Uses the 'fst' package to store genotype probabilities on disk for the 'qtl2' package. These genotype probabilities are a central data object for mapping quantitative trait loci (QTL), but they can be quite large. The facilities in this package enable the genotype probabilities to be stored on disk, leading to reduced memory usage with only a modest increase in computation time.
	"""
	
	homepage = "https://github.com/rqtl/qtl2fst"
	cran = "qtl2fst" 

	version("0.26", md5="bd124a72fb05da5ada25f215b2711785")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-fst", type=("build", "run"))
	depends_on("r-qtl2@0.24:", type=("build", "run"))
