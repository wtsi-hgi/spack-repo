# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRamr(RPackage):
	"""Detection of Rare Aberrantly Methylated Regions in Array and NGS Data

	ramr is an R package for detection of low-frequency aberrant methylation events in large data sets obtained by methylation profiling using array or high-throughput bisulfite sequencing. In addition, package provides functions to visualize found aberrantly methylated regions (AMRs), to generate sets of all possible regions to be used as reference sets for enrichment analysis, and to generate biologically relevant test data sets for performance evaluation of AMR/DMR search algorithms.
	"""
	
	homepage = "https://github.com/BBCG/ramr"
	bioc = "ramr"

	version("1.16.0", commit="a19305bc3061062ece0985747cb04d87001ff433")
	version("1.10.0", commit="4a632c193c27d7ec9b206cc2eb34fbde9bf3e6b9")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-envstats", type=("build", "run"))
	depends_on("r-extdist", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
