# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtn(RPackage):
	"""RTN: Reconstruction of Transcriptional regulatory Networks and analysis of regulons

	A transcriptional regulatory network (TRN) consists of a collection of transcription factors (TFs) and the regulated target genes. TFs are regulators that recognize specific DNA sequences and guide the expression of the genome, either activating or repressing the expression the target genes. The set of genes controlled by the same TF forms a regulon. This package provides classes and methods for the reconstruction of TRNs and analysis of regulons.
	"""
	
	homepage = "http://dx.doi.org/10.1038/ncomms3464"
	bioc = "RTN" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/RTN_2.26.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/RTN/RTN_2.26.0.tar.gz"]

    version("2.32.0", tag="RELEASE_3_21")
	version("2.26.0", sha256="c50386259d4a92e9c56b68c696fae72831dd411c83d3b8cf618ad495375c90d6")

	depends_on("r@3.6.3:", type=("build", "run"))
	depends_on("r-reder", type=("build", "run"))
	depends_on("r-minet", type=("build", "run"))
	depends_on("r-viper", type=("build", "run"))
	depends_on("r-mixtools", type=("build", "run"))
	depends_on("r-snow", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-pwr", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
