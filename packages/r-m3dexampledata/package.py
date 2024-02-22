# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RM3dexampledata(RPackage):
	"""M3Drop Example Data

	Example data for M3Drop package.
	"""
	
	bioc = "M3DExampleData" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/M3DExampleData_1.28.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/M3DExampleData/M3DExampleData_1.28.0.tar.gz"]

	version("1.28.0", md5="6988767aab7572ae3e701fd6854c061f")

	depends_on("r@3.3:", type=("build", "run"))

	# experiment