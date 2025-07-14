# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiffutr(RPackage):
	"""diffUTR: Streamlining differential exon and 3' UTR usage

	The diffUTR package provides a uniform interface and plotting functions for limma/edgeR/DEXSeq -powered differential bin/exon usage. It includes in addition an improved version of the limma::diffSplice method. Most importantly, diffUTR further extends the application of these frameworks to differential UTR usage analysis using poly-A site databases.
	"""
	
	bioc = "diffUTR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/diffUTR_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/diffUTR/diffUTR_1.10.0.tar.gz"]

    version("1.16.0", tag="RELEASE_3_21")
	version("1.10.0", sha256="929c164ac14bc0418e76e7ae05eedd6e5d1312153344b2b0e7f25e6e4c86c67d")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-dexseq", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-rsubread", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-ensembldb", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
