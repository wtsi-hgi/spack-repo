# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDplr(RPackage):
	"""Dendrochronology Program Library in R

	Perform tree-ring analyses such as detrending, chronology
        building, and cross dating.  Read and write standard file formats
        used in dendrochronology.
	"""
	
	homepage = "https://github.com/AndyBunn/dplR"
	cran = "dplR" 

	version("1.7.6", md5="b3b280f6f5ff2f4ede5c90b1ae6b61c8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lattice@0.13.6:", type=("build", "run"))
	depends_on("r-matrix@1.0.3:", type=("build", "run"))
	depends_on("r-digest@0.2.3:", type=("build", "run"))
	depends_on("r-matrixstats@0.50.2:", type=("build", "run"))
	depends_on("r-png@0.1.2:", type=("build", "run"))
	depends_on("r-r-utils@1.32.1:", type=("build", "run"))
	depends_on("r-stringi@0.2.3:", type=("build", "run"))
	depends_on("r-stringr@0.4:", type=("build", "run"))
	depends_on("r-xml@2.1.0:", type=("build", "run"))
	depends_on("r-plyr@1.8:", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
