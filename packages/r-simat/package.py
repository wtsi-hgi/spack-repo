# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimat(RPackage):
	"""GC-SIM-MS data processing and alaysis tool

	This package provides a pipeline for analysis of GC-MS data acquired in selected ion monitoring (SIM) mode. The tool also provides a guidance in choosing appropriate fragments for the targets of interest by using an optimization algorithm. This is done by considering overlapping peaks from a provided library by the user.
	"""
	
	homepage = "http://omics.georgetown.edu/SIMAT.html"
	bioc = "SIMAT"

	version("1.40.0", commit="a1040c6f2b3853c301e76c22be95429f90fc08ea")
	version("1.34.0", commit="6811bf1a0da1ab18289eb35090f5e47fa05741ff")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp@0.11.3:", type=("build", "run"))
	depends_on("r-mzr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
