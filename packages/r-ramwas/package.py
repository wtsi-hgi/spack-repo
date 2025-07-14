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

	version("1.32.0", commit="eff59d653d717eb76de47bd9667e3111caa6c524")
	version("1.26.0", commit="cb4c07218c8c025f27984b69fc4651fdd9d6a466")

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
