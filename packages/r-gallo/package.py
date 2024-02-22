# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGallo(RPackage):
	"""Genomic Annotation in Livestock for Positional Candidate LOci

	The accurate annotation of genes and Quantitative Trait Loci (QTLs) located within candidate markers and/or regions (haplotypes, windows, CNVs, etc) is a crucial step the most common genomic analyses performed in livestock, such as Genome-Wide Association Studies or transcriptomics. The Genomic Annotation in Livestock for positional candidate LOci (GALLO) is an R package designed to provide an intuitive and straightforward environment to annotate positional candidate genes and QTLs from high-throughput genetic studies in livestock. Moreover, GALLO allows the graphical visualization of gene and QTL annotation results, data comparison among different grouping factors (e.g., methods, breeds, tissues, statistical models, studies, etc.), and QTL enrichment in different livestock species including cattle, pigs, sheep, and chicken, among others.
	"""
	
	homepage = "<https://github.com/pablobio/GALLO>"
	cran = "GALLO" 

	version("1.3", md5="54fa98a37770837c010ce219e4340603")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-unbalhaar", type=("build", "run"))
	depends_on("r-webshot", type=("build", "run"))
