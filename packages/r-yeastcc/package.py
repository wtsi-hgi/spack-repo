# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYeastcc(RPackage):
	"""Spellman et al. (1998) and Pramila/Breeden (2006) yeast cell cycle microarray data

	ExpressionSet for Spellman et al. (1998) yeast cell cycle microarray experiment
	"""
	
	bioc = "yeastCC" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/yeastCC_1.42.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/yeastCC/yeastCC_1.42.0.tar.gz"]

    version("1.48.0", tag="RELEASE_3_21")
	version("1.42.0", sha256="d6654c09539b2a8a84d0e07c8e984fa97763f3760b78acafabeddbcfa91c74a9")

	depends_on("r-biobase@2.5.5:", type=("build", "run"))

