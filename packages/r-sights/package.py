# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSights(RPackage):
	"""Statistics and dIagnostic Graphs for HTS

	SIGHTS is a suite of normalization methods, statistical tests, and diagnostic graphical tools for high throughput screening (HTS) assays. HTS assays use microtitre plates to screen large libraries of compounds for their biological, chemical, or biochemical activity.
	"""
	
	homepage = "https://eg-r.github.io/sights/"
	bioc = "sights" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/sights_1.28.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/sights/sights_1.28.0.tar.gz"]

	version("1.34.0", tag="RELEASE_3_21")
	version("1.28.0", sha256="1997ca79956d3d07ddab78e092b87ff7e78149b54abc0d792e0abe9d19ecb8c4")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-mass@7.3:", type=("build", "run"))
	depends_on("r-qvalue@2.2:", type=("build", "run"))
	depends_on("r-ggplot2@2:", type=("build", "run"))
	depends_on("r-reshape2@1.4:", type=("build", "run"))
	depends_on("r-lattice@0.2:", type=("build", "run"))
