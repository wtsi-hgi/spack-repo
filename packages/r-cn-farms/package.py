# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCnFarms(RPackage):
	"""cn.FARMS - factor analysis for copy number estimation

	This package implements the cn.FARMS algorithm for copy number variation (CNV) analysis. cn.FARMS allows to analyze the most common Affymetrix (250K-SNP6.0) array types, supports high-performance computing using snow and ff.
	"""
	
	homepage = "http://www.bioinf.jku.at/software/cnfarms/cnfarms.html"
	bioc = "cn.farms"

	version("1.56.0", commit="918644e1cabeb41d221cf75c49cdebdae6b06638")
	version("1.50.0", commit="98df0d513ee5432e00092e4b7230020f23c4ebea")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-ff", type=("build", "run"))
	depends_on("r-oligoclasses", type=("build", "run"))
	depends_on("r-snow", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-affxparser", type=("build", "run"))
	depends_on("r-oligo", type=("build", "run"))
	depends_on("r-dnacopy", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
