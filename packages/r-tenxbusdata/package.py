# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTenxbusdata(RPackage):
	"""Single cell dataset from 10x in BUS format

	Download Barcode, UMI, and Set (BUS) format of 10x datasets from within R. This package accompanies the package BUSpaRse, which can load BUS format into R as a sparse matrix, and which has utility functions related to using the C++ command line package bustools.
	"""
	
	homepage = "https://github.com/BUStools/TENxBUSData"
	bioc = "TENxBUSData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/TENxBUSData_1.16.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/TENxBUSData/TENxBUSData_1.16.0.tar.gz"]

	version("1.16.0", md5="35be2bd3c806b055fc9463e8f135dd32")

	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))

	# experiment