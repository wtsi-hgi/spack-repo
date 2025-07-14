# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR3cpet(RPackage):
	"""3CPET: Finding Co-factor Complexes in Chia-PET experiment using a Hierarchical Dirichlet Process

	The package provides a method to infer the set of proteins that are more probably to work together to maintain chormatin interaction given a ChIA-PET experiment results.
	"""
	
	bioc = "R3CPET"

	version("1.40.0", commit="36fe80f2fbda926ad5724de3c4ed34437a385384")
	version("1.34.1", commit="5578c0641ed1ef8d4cf631cac6545fe3c9c53cf0")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-clvalid", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges@2.13.12:", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicranges@1.31.8:", type=("build", "run"))
	depends_on("r-ggbio", type=("build", "run"))
