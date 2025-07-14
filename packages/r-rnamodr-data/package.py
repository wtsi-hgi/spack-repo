# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnamodrData(RPackage):
	"""Example data for the RNAmodR package

	RNAmodR.Data contains example data, which is used for vignettes and example workflows in the RNAmodR and dependent packages.
	"""
	
	homepage = "https://github.com/FelixErnst/RNAmodR.Data"
	bioc = "RNAmodR.Data" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/RNAmodR.Data_1.16.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/RNAmodR.Data/RNAmodR.Data_1.16.0.tar.gz"]

    version("1.22.0", tag="RELEASE_3_21")
	version("1.16.0", sha256="0159cb46031193ee09916fd929562a5a2c23e201bf4017b7552b0495890c3d5d")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-experimenthubdata@1.9.2:", type=("build", "run"))

