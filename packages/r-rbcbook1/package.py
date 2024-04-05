# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbcbook1(RPackage):
	"""Support for Springer monograph on Bioconductor

	tools for building book
	"""
	
	homepage = "http://www.biostat.harvard.edu/~carey"
	bioc = "RbcBook1" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/RbcBook1_1.70.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/RbcBook1/RbcBook1_1.70.0.tar.gz"]

	version("1.70.0", md5="16f681613c1c4d309b032c64cfe18c4a", url="https://www.bioconductor.org/packages/release/bioc/src/contrib/RbcBook1_1.70.0.tar.gz")
	version("1.70.0", md5="16f681613c1c4d309b032c64cfe18c4a", url="https://www.bioconductor.org/packages/3.18/bioc/src/contrib/RbcBook1_1.70.0.tar.gz")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
