# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgu2beta7(RPackage):
	"""A data package containing annotation data for hgu2beta7

	Annotation data file for hgu2beta7 assembled using data from public data repositories
	"""
	
	bioc = "hgu2beta7" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/hgu2beta7_1.42.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/hgu2beta7/hgu2beta7_1.42.0.tar.gz"]

	version("1.42.0", sha256="d731d63655ec8e2d8ca2af2b2fb4e567791144c3bd3c2578f5c603731a91bcf7", url="https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/hgu2beta7_1.42.0.tar.gz")

	depends_on("r@2:", type=("build", "run"))

