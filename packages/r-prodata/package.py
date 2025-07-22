# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProdata(RPackage):
	"""SELDI-TOF data of Breast cancer samples

	A data package of SELDI-TOF protein mass spectrometry data of 167 breast cancer and normal samples.
	"""
	
	bioc = "ProData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/ProData_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/ProData/ProData_1.40.0.tar.gz"]

	version("1.46.0", tag="RELEASE_3_21")
	version("1.40.0", sha256="6296eb2fe5ed73a2bab4a09722027955beb033d7b4c1b02c395fcc4102723d25")

	depends_on("r@2.4:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))

