# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiodist(RPackage):
	"""Different distance measures

	A collection of software tools for calculating distance measures.
	"""
	
	bioc = "bioDist" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/bioDist_1.74.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/bioDist/bioDist_1.74.0.tar.gz"]

	version("1.74.0", md5="a0c907dc82834b4771074cd8164cf773")

	depends_on("r@2:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
