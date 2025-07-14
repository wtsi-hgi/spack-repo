# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RM3drop(RPackage):
	"""Michaelis-Menten Modelling of Dropouts in single-cell RNASeq

	This package fits a Michaelis-Menten model to the pattern of dropouts in single-cell RNASeq data. This model is used as a null to identify significantly variable (i.e. differentially expressed) genes for use in downstream analysis, such as clustering cells.
	"""
	
	homepage = "https://github.com/tallulandrews/M3Drop"
	bioc = "M3Drop" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/M3Drop_1.28.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/M3Drop/M3Drop_1.28.0.tar.gz"]

    version("1.34.0", tag="RELEASE_3_21")
	version("1.28.0", md5="ad347f93f1a297543e7ab0e74437dd4d")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-bbmle", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-reldist", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
