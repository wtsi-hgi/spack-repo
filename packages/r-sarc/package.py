# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSarc(RPackage):
	"""Statistical Analysis of Regions with CNVs

	Imports a cov/coverage file (normalised read coverages from BAM files) and a cnv file (list of CNVs - similiar to a BED file) from WES/ WGS CNV (copy number variation) detection pipelines and utilises several metrics to weigh the likelihood of a sample containing a detected CNV being a true CNV or a false positive. Highly useful for diagnostic testing to filter out false positives to provide clinicians with fewer variants to interpret. SARC uniquely only used cov and csv (similiar to BED file) files which are the common CNV pipeline calling filetypes, and can be used as to supplement the Interactive Genome Browser (IGV) to generate many figures automatedly, which can be especially helpful in large cohorts with 100s-1000s of patients.
	"""
	
	homepage = "https://github.com/Krutik6/SARC/"
	bioc = "SARC" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/SARC_1.0.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/SARC/SARC_1.0.0.tar.gz"]

    version("1.6.0", tag="RELEASE_3_21")
	version("1.0.0", sha256="5f032cedb91ca13f975da592479c83ff79c87c3ba5dd4472c1c7df0b9cec7a10")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-raggedexperiment", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-desctools", type=("build", "run"))
	depends_on("r-metap", type=("build", "run"))
	depends_on("r-multtest", type=("build", "run"))
	depends_on("r-plyranges", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
