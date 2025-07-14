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

    version("1.76.0", tag="RELEASE_3_21")
	version("1.70.0", sha256="11702d6c99be1015f812a0d9a63cbca1beeaca0e7e0dedca49588a2136067f75", url="https://www.bioconductor.org/packages/3.18/bioc/src/contrib/RbcBook1_1.70.0.tar.gz")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
