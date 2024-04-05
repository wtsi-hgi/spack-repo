# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMerfishdata(RPackage):
	"""Collection of public MERFISH datasets

	MerfishData is an ExperimentHub package that serves publicly available datasets obtained with Multiplexed Error-Robust Fluorescence in situ Hybridization (MERFISH). MERFISH is a massively multiplexed single-molecule imaging technology capable of simultaneously measuring the copy number and spatial distribution of hundreds to tens of thousands of RNA species in individual cells. The scope of the package is to provide MERFISH data for benchmarking and analysis.
	"""
	
	homepage = "https://github.com/ccb-hms/MerfishData"
	bioc = "MerfishData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/MerfishData_1.4.1.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/MerfishData/MerfishData_1.4.1.tar.gz"]

	version("1.4.1", md5="05369f89c4e1a15bdab1ce5174facbe4")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-ebimage", type=("build", "run"))
	depends_on("r-spatialexperiment", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-bumpymatrix", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))

