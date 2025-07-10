# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRestfulsedata(RPackage):
	"""Example metadata for the "restfulSE" R package

	Metadata RangedSummarizedExperiment shell for use with restfulSE.
	"""
	
	bioc = "restfulSEData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/restfulSEData_1.24.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/restfulSEData/restfulSEData_1.24.0.tar.gz"]

	version("1.24.0", sha256="302d8f15602430563a75fa25e57a7b1b0b761f8e129792e43856efbd2a29b1f9")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-delayedarray@0.21.2:", type=("build", "run"))
	depends_on("r-hdf5array@1.23.2:", type=("build", "run"))

