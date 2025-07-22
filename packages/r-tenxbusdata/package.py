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

	version("1.22.0", tag="RELEASE_3_21")
	version("1.16.0", sha256="f6a0de55b9409f4efedd2139bb507a79551874ae991a4a0c337afdad005e381c")

	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))

