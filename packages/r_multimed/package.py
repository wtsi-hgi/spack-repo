# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultimed(RPackage):
	"""Testing multiple biological mediators simultaneously

	Implements methods for testing multiple mediators
	"""
	
	bioc = "MultiMed" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MultiMed_2.24.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MultiMed/MultiMed_2.24.0.tar.gz"]

	version("2.24.0", md5="019bc5d7be15d1688b3b5df7b87246f7")

	depends_on("r@3.1:", type=("build", "run"))
