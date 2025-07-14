# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMipp(RPackage):
	"""Misclassification Penalized Posterior Classification

	This package finds optimal sets of genes that seperate samples into two or more classes.
	"""
	
	homepage = "http://www.healthsystem.virginia.edu/internet/hes/biostat/bioinformatics/"
	bioc = "MiPP" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MiPP_1.74.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MiPP/MiPP_1.74.0.tar.gz"]

	version("1.80.0", tag="RELEASE_3_21")
	version("1.74.0", sha256="8241ed264ea0462b550342e76a74d688b6a18b39e8e45d82a85f561046f761ff")

	depends_on("r@2.4:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
