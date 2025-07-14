# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnifter(RPackage):
	"""R wrapper for the python openTSNE library

	Provides an R wrapper for the implementation of FI-tSNE from the python package openTNSE. See Poličar et al. (2019) <doi:10.1101/731877> and the algorithm described by Linderman et al. (2018) <doi:10.1038/s41592-018-0308-4>.
	"""
	
	homepage = "https://bioconductor.org/packages/snifter"
	bioc = "snifter" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/snifter_1.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/snifter/snifter_1.12.0.tar.gz"]

	version("1.18.1", tag="RELEASE_3_21")
	version("1.12.0", sha256="2205ceb73a1cb1980b9d91be6c1dc61a91bc11b04f7e5cf974621d664025d2f8")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-basilisk", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
