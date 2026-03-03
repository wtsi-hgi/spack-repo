# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCctutorial(RPackage):
	"""Data package for ChIP-chip tutorial

	This is a data package that accompanies a ChIP-chip tutorial, which has been published in PLoS Computational Biology. The data and source code in this package allow the reader to completely reproduce the steps in the tutorial.
	"""
	
	bioc = "ccTutorial" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/ccTutorial_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/ccTutorial/ccTutorial_1.40.0.tar.gz"]

	version("1.40.0", md5="20af731ec83a03f12ec5d87060f5d168")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ringo@1.9.8:", type=("build", "run"))
	depends_on("r-affy@1.23.4:", type=("build", "run"))
	depends_on("r-topgo@1.13.1:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))

