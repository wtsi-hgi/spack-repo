# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPepsnmrdata(RPackage):
	"""Datasets for the PepsNMR package

	This package contains all the datasets used in the PepsNMR package.
	"""
	
	bioc = "PepsNMRData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/PepsNMRData_1.20.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/PepsNMRData/PepsNMRData_1.20.0.tar.gz"]

	version("1.26.0", tag="RELEASE_3_21")
	version("1.20.0", sha256="ac94ca39bb77784f15bd5dc645df43a6329e49f2296bb98016347f2b9a2fc0f7")

	depends_on("r@3.5:", type=("build", "run"))

