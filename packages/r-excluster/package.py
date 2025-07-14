# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExcluster(RPackage):
	"""ExCluster robustly detects differentially expressed exons between two conditions of RNA-seq data, requiring at least two independent biological replicates per condition

	ExCluster flattens Ensembl and GENCODE GTF files into GFF files, which are used to count reads per non-overlapping exon bin from BAM files. This read counting is done using the function featureCounts from the package Rsubread. Library sizes are normalized across all biological replicates, and ExCluster then compares two different conditions to detect signifcantly differentially spliced genes. This process requires at least two independent biological repliates per condition, and ExCluster accepts only exactly two conditions at a time. ExCluster ultimately produces false discovery rates (FDRs) per gene, which are used to detect significance. Exon log2 fold change (log2FC) means and variances may be plotted for each significantly differentially spliced gene, which helps scientists develop hypothesis and target differential splicing events for RT-qPCR validation in the wet lab.
	"""
	
	bioc = "ExCluster"

	version("1.26.0", commit="8785161ee9394a367ee51b921544d8a2a7082f06")
	version("1.20.0", commit="ccabcb57c5b3e73689bbea47b6c54fa5da03861e")

	depends_on("r-rsubread", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
