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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/R3CPET_1.34.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/R3CPET/R3CPET_1.34.1.tar.gz"]

    version("1.40.0", tag="RELEASE_3_21")
	version("1.34.1", sha256="4861a3e236229212150e1b17bc75239783250986cef4759ae64e7b63b4d9192c")

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
