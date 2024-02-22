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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/RITAN_1.26.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/RITAN/RITAN_1.26.0.tar.gz"]

	version("1.26.0", md5="d9b8cf771e70cd374ba72e63aa439865")

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
