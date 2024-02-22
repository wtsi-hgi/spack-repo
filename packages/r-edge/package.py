# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REdge(RPackage):
	"""Extraction of Differential Gene Expression

	The edge package implements methods for carrying out differential expression analyses of genome-wide gene expression studies. Significance testing using the optimal discovery procedure and generalized likelihood ratio tests (equivalent to F-tests and t-tests) are implemented for general study designs. Special functions are available to facilitate the analysis of common study designs, including time course experiments. Other packages such as snm, sva, and qvalue are integrated in edge to provide a wide range of tools for gene expression analysis.
	"""
	
	homepage = "https://github.com/jdstorey/edge"
	bioc = "edge" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/edge_2.34.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/edge/edge_2.34.0.tar.gz"]

	version("2.34.0", md5="89d1683b6b4f9723b4c4fcef6972d543")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-sva", type=("build", "run"))
	depends_on("r-snm", type=("build", "run"))
	depends_on("r-qvalue@1.99:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
