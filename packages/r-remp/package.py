# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRemp(RPackage):
	"""Repetitive Element Methylation Prediction

	Machine learning-based tools to predict DNA methylation of locus-specific repetitive elements (RE) by learning surrounding genetic and epigenetic information. These tools provide genomewide and single-base resolution of DNA methylation prediction on RE that are difficult to measure using array-based or sequencing-based platforms, which enables epigenome-wide association study (EWAS) and differentially methylated region (DMR) analysis on RE.
	"""
	
	homepage = "https://github.com/YinanZheng/REMP"
	bioc = "REMP"

	version("1.32.1", commit="432f6f631673ab32bf7baa237340f8865af8792f")
	version("1.26.0", commit="ee4ee19e4fd4a36cde2c37ad2ecde7ec5cb76374")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-summarizedexperiment@1.1.6:", type=("build", "run"))
	depends_on("r-minfi@1.22:", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-settings", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-impute", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
