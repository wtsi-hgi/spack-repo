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
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/PepsNMRData_1.20.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/PepsNMRData/PepsNMRData_1.20.0.tar.gz"]

	version("1.20.0", md5="96fc9090499b4460f72fb85a0428b357")

	depends_on("r@3.5:", type=("build", "run"))

	# experiment