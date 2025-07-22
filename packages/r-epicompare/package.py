# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpicompare(RPackage):
	"""Comparison, Benchmarking & QC of Epigenomic Datasets

	EpiCompare is used to compare and analyse epigenetic datasets for quality control and benchmarking purposes. The package outputs an HTML report consisting of three sections: (1. General metrics) Metrics on peaks (percentage of blacklisted and non-standard peaks, and peak widths) and fragments (duplication rate) of samples, (2. Peak overlap) Percentage and statistical significance of overlapping and non-overlapping peaks. Also includes upset plot and (3. Functional annotation) functional annotation (ChromHMM, ChIPseeker and enrichment analysis) of peaks. Also includes peak enrichment around TSS.
	"""
	
	homepage = "https://github.com/neurogenomics/EpiCompare"
	bioc = "EpiCompare"

	version("1.12.0", commit="f21c667278b04113ab779b3303e230e142fdb170")
	version("1.6.7", commit="6ea246afe6d59cc02aaf3c8cf2467041e1b42f02")
	version("1.6.5", md5="27be81e1f3112ca55bab8460e2f191b7")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-brgenomics", type=("build", "run"))
	depends_on("r-chipseeker", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-genomation", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-ggplot2@3.5:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-downloadthis", type=("build", "run"))
