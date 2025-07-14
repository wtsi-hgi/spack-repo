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

	version("1.22.0", commit="285e716647aa5078a79f5d2bd7cff18888d0f421")
	version("1.16.0", commit="8f20078a9fe469631cdc10604fc9d9726e3f0a2d")

	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))

