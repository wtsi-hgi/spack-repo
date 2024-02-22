# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetgsa(RPackage):
	"""Network-Based Gene Set Analysis

	Carry out network-based gene set analysis by incorporating external information about interactions among genes, as well as novel interactions learned from data. Implements methods described in Shojaie A, Michailidis G (2010) <doi:10.1093/biomet/asq038>, Shojaie A, Michailidis G (2009) <doi:10.1089/cmb.2008.0081>, and Ma J, Shojaie A, Michailidis G (2016) <doi:10.1093/bioinformatics/btw410>.
	"""
	
	homepage = "https://github.com/mikehellstern/netgsa"
	cran = "netgsa" 

	version("4.0.5", md5="96e9f258f050837f74569670c5dcd966")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-genefilter", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-graphite", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-glassofast", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-msigdbr", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-rcy3", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
