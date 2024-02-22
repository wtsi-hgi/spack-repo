# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRamwas(RPackage):
	"""Fast Methylome-Wide Association Study Pipeline for Enrichment Platforms

	A complete toolset for methylome-wide association studies (MWAS). It is specifically designed for data from enrichment based methylation assays, but can be applied to other data as well. The analysis pipeline includes seven steps: (1) scanning aligned reads from BAM files, (2) calculation of quality control measures, (3) creation of methylation score (coverage) matrix, (4) principal component analysis for capturing batch effects and detection of outliers, (5) association analysis with respect to phenotypes of interest while correcting for top PCs and known covariates, (6) annotation of significant findings, and (7) multi-marker analysis (methylation risk score) using elastic net. Additionally, RaMWAS include tools for joint analysis of methlyation and genotype data. This work is published in Bioinformatics, Shabalin et al. (2018) <doi:10.1093/bioinformatics/bty069>.
	"""
	
	homepage = "https://bioconductor.org/packages/ramwas/"
	bioc = "ramwas" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/ramwas_1.26.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/ramwas/ramwas_1.26.0.tar.gz"]

	version("1.26.0", md5="ccbff0a1c4bd31c8ceb9d2641d6608d2")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-filematrix", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
