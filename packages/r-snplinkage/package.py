# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnplinkage(RPackage):
	"""Single Nucleotide Polymorphisms Linkage Disequilibrium
Visualizations

	Linkage disequilibrium visualizations of up to several hundreds of single nucleotide polymorphisms (SNPs), annotated with chromosomic positions and gene names. Two types of plots are available for small numbers of SNPs (<40) and for large numbers (tested up to 500). Both can be extended by combining other ggplots, e.g. association studies results, and functions enable to directly visualize the effect of SNP selection methods, as minor allele frequency filtering and TagSNP selection, with a second correlation heatmap. The SNPs correlations are computed on Genotype Data objects from the 'GWASTools' package using the 'SNPRelate' package, and the plots are customizable 'ggplot2' and 'gtable' objects and are annotated using the 'biomaRt' package. Usage is detailed in the vignette with example data and results from up to 500 SNPs of 1,200 scans are in Charlon T. (2019) <doi:10.13097/archive-ouverte/unige:161795>.
	"""
	
	homepage = "https://gitlab.com/thomaschln/snplinkage"
	cran = "snplinkage" 

	version("1.0.0", md5="044c4b7eeb79083ef754a6543524d9f6")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-gwastools@1.10.1:", type=("build", "run"))
	depends_on("r-gdsfmt", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
