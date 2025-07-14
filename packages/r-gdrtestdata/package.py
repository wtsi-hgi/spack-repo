# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGdrtestdata(RPackage):
	"""gDRtestData - R data package with testing dose reponse data

	R package with internal dose-response test data. Package provides functions to generate input testing data that can be used as the input for gDR pipeline. It also contains RDS files with MAE data processed by gDR.
	"""
	
	bioc = "gDRtestData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/gDRtestData_1.0.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/gDRtestData/gDRtestData_1.0.0.tar.gz"]

	version("1.6.0", tag="RELEASE_3_21")
	version("1.0.0", sha256="19b06102d2720e5d2b423a98b7075fecf22b7769314ed64c6379c3c0f6f5995f")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))

