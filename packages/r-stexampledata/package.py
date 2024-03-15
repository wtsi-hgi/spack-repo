# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStexampledata(RPackage):
	"""Collection of spatially-resolved transcriptomics datasets in SpatialExperiment Bioconductor format

	Collection of spatially-resolved transcriptomics (SRT) datasets in SpatialExperiment Bioconductor format, for use in examples, demonstrations, and tutorials. The datasets are from several different SRT platforms and have been sourced from various publicly available sources. Several datasets include images and/or ground truth annotation labels.
	"""
	
	homepage = "https://github.com/lmweber/STexampleData"
	bioc = "STexampleData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/STexampleData_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/STexampleData/STexampleData_1.10.0.tar.gz"]

	version("1.10.0", md5="5fa4bfb2e58e7f6bbcd957aa1aa7e938")

	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-spatialexperiment", type=("build", "run"))

	# experiment