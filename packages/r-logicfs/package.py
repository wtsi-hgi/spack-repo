# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLogicfs(RPackage):
	"""Identification of SNP Interactions

	Identification of interactions between binary variables using Logic Regression. Can, e.g., be used to find interesting SNP interactions. Contains also a bagging version of logic regression for classification.
	"""
	
	bioc = "logicFS" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/logicFS_2.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/logicFS/logicFS_2.22.0.tar.gz"]

	version("2.28.0", tag="RELEASE_3_21")
	version("2.22.0", sha256="783731537784c6cd55a5b192b35040d3a7978d3fb80228a9380dea0ab1001c8d")

	depends_on("r-logicreg", type=("build", "run"))
	depends_on("r-mcbiopi", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
