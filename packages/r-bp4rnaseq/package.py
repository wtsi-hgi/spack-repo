# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBp4rnaseq(RPackage):
	"""A babysitter's package for reproducible RNA-seq analysis

	An automated pipe for reproducible RNA-seq analysis with the minimal efforts from researchers. The package can process bulk RNA-seq data and single-cell RNA-seq data. You can only provide the taxa name and the accession id of RNA-seq data deposited in the National Center for Biotechnology Information (NCBI). After a cup of tea or longer, you will get formated gene expression data as gene count and transcript count based on both alignment-based and alignment-free workflows.
	"""
	
	bioc = "BP4RNAseq"

	version("1.18.0", commit="9994b606732da2c9897e06838ea60dd59c827851")
	version("1.12.0", commit="91f397ad487b553f5c1ff18816087c4a930686e7")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fastqcr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("sratoolkit@2.10.3:", type=("build", "link", "run"))
	depends_on("entrezdirect", type=("build", "link", "run"))
	depends_on("fastqc@0.11.9:", type=("build", "link", "run"))
	depends_on("py-cutadapt@2.10:", type=("build", "link", "run"))
	depends_on("py-datasets", type=("build", "link", "run"))
	depends_on("samtools@1.9:", type=("build", "link", "run"))
	depends_on("hisat2@2.2.0:", type=("build", "link", "run"))
	depends_on("stringtie@2.1.1:", type=("build", "link", "run"))
	depends_on("salmon@1.2.1:", type=("build", "link", "run"))

