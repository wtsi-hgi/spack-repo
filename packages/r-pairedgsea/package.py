# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPairedgsea(RPackage):
	"""Paired DGE and DGS analysis for gene set enrichment analysis

	pairedGSEA makes it simple to run a paired Differential Gene Expression (DGE) and Differencital Gene Splicing (DGS) analysis. The package allows you to store intermediate results for further investiation, if desired. pairedGSEA comes with a wrapper function for running an Over-Representation Analysis (ORA) and functionalities for plotting the results.
	"""
	
	homepage = "https://github.com/shdam/pairedGSEA"
	bioc = "pairedGSEA" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/pairedGSEA_1.2.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/pairedGSEA/pairedGSEA_1.2.0.tar.gz"]

	version("1.8.0", tag="RELEASE_3_21")
	version("1.2.0", sha256="bead1ecc8d1cc2f4e370ec6062bc0a873a5b2cce3818937c5c6a1bb7e02b97d1")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-dexseq", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-fgsea", type=("build", "run"))
	depends_on("r-sva", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-aggregation", type=("build", "run"))
