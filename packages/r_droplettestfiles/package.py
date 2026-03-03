# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDroplettestfiles(RPackage):
	"""Test Files for Single-Cell Droplet Utilities

	Assorted files generated from droplet-based single-cell protocols, to be used for testing functions in DropletUtils. Primarily intended for storing files that directly come out of processing pipelines like 10X Genomics' CellRanger software, prior to the formation of a SingleCellExperiment object. Unlike other packages, this is not designed to provide objects that are immediately ready for analysis.
	"""
	
	bioc = "DropletTestFiles" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/DropletTestFiles_1.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/DropletTestFiles/DropletTestFiles_1.12.0.tar.gz"]

	version("1.12.0", md5="5a3a3f0d0901c90c6a2b173b976c4868")

	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))

