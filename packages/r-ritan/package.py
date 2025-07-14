# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRitan(RPackage):
	"""Rapid Integration of Term Annotation and Network resources

	Tools for comprehensive gene set enrichment and extraction of multi-resource high confidence subnetworks. RITAN facilitates bioinformatic tasks for enabling network biology research.
	"""
	
	bioc = "RITAN"

	version("1.32.0", commit="5350c536aa36a96de7f1ef8089cc76d07ba66b4a")
	version("1.26.0", commit="13a63fd9f0a70320adfcc33c3921b3a9a0e96da0")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-stringdb", type=("build", "run"))
	depends_on("r-mcl", type=("build", "run"))
	depends_on("r-linkcomm", type=("build", "run"))
	depends_on("r-dynamictreecut", type=("build", "run"))
	depends_on("r-gsubfn", type=("build", "run"))
	depends_on("r-hash", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-sqldf", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-bgeedb", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-ritandata", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-ensembldb", type=("build", "run"))
	depends_on("r-annotationfilter", type=("build", "run"))
	depends_on("r-ensdb-hsapiens-v86", type=("build", "run"))
