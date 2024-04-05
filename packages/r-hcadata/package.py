# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHcadata(RPackage):
	"""Accessing The Datasets Of The Human Cell Atlas in R/Bioconductor

	This package allows a direct access to the dataset generated by the Human Cell Atlas project for further processing in R and Bioconductor, in the comfortable format of SingleCellExperiment objects (available in other formats here: http://preview.data.humancellatlas.org/).
	"""
	
	homepage = "https://github.com/federicomarini/HCAData"
	bioc = "HCAData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/HCAData_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/HCAData/HCAData_1.18.0.tar.gz"]

	version("1.18.0", md5="4f16bf5904ca21c0fb0bd6515d7ab4d3")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-hdf5array", type=("build", "run"))

