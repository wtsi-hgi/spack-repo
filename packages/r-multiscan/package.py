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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/multiscan_1.62.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/multiscan/multiscan_1.62.0.tar.gz"]

	version("1.62.0", sha256="9193d18c5ecf8465b44edddac53008b509a0bba4cce6a5e1d8050975e1d05027")

	depends_on("r@2.3:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
