# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDmrcate(RPackage):
	"""Methylation array and sequencing spatial analysis methods.

	De novo identification and extraction of differentially methylated regions
	(DMRs) from the human genome using Whole Genome Bisulfite Sequencing (WGBS)
	and Illumina Infinium Array (450K and EPIC) data. Provides functionality
	for filtering probes possibly confounded by SNPs and cross-hybridisation.
	Includes GRanges generation and plotting functions."""

	bioc = "DMRcate"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/DMRcate_2.16.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/DMRcate/DMRcate_2.16.1.tar.gz"]
	version("2.8.5", commit="c65dc79a33a047c10932a98b3383709a6bcb8903")
	version("2.4.1", commit="bc6242a0291a9b997872f575a4417d38550c9550")
	version("2.16.1", md5="6c37b23c3dc4f68915ab665f3572ad95")
	version("2.14.0", commit="6e7bae0917001e7664f01c3f8d261f9fe28c2f4d")
	version("2.12.0", commit="560dd5067b05715631739d0fb58ef9cebdbf7078")
	version("2.10.0", commit="81e83701da5c55ac83d0e0b5e640a9d431f09551")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-bsseq", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-minfi", type=("build", "run"))
	depends_on("r-missmethyl", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-gviz", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
