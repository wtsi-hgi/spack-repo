# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultiscan(RPackage):
	"""R package for combining multiple scans

	Estimates gene expressions from several laser scans of the same microarray
	"""
	
	bioc = "multiscan" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/multiscan_1.62.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/multiscan/multiscan_1.62.0.tar.gz"]

	version("1.62.0", md5="58243690ff05bdbd30da46ea01e409a3")

	depends_on("r@2.3:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
