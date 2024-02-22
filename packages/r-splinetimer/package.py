# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSplinetimer(RPackage):
	"""Time-course differential gene expression data analysis using spline regression models followed by gene association network reconstruction

	This package provides functions for differential gene expression analysis of gene expression time-course data. Natural cubic spline regression models are used. Identified genes may further be used for pathway enrichment analysis and/or the reconstruction of time dependent gene regulatory association networks.
	"""
	
	bioc = "splineTimeR" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/splineTimeR_1.30.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/splineTimeR/splineTimeR_1.30.0.tar.gz"]

	version("1.30.0", md5="09454e29df75ff3f9d9e3f2780fb5db6")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-gseabase", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-genenet@1.2.13:", type=("build", "run"))
	depends_on("r-longitudinal@1.1.12:", type=("build", "run"))
	depends_on("r-fis", type=("build", "run"))
