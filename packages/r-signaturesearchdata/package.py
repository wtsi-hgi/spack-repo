# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSignaturesearchdata(RPackage):
	"""Datasets for signatureSearch package

	CMAP/LINCS hdf5 databases and other annotations used for signatureSearch software package.
	"""
	
	bioc = "signatureSearchData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/signatureSearchData_1.16.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/signatureSearchData/signatureSearchData_1.16.0.tar.gz"]

	version("1.22.0", tag="RELEASE_3_21")
	version("1.16.0", sha256="7f6892c6f4eca33e68969eacbbdbe9947708b0eb4bfdaf52279acccbeaf1c0f6")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))

