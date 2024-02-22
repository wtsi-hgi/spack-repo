# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDatacombine(RPackage):
	"""Tools for Easily Combining and Cleaning Data Sets

	Tools for combining and cleaning data sets, particularly
    with grouped and time series data.
	"""
	
	homepage = "http://CRAN.R-project.org/package=DataCombine"
	cran = "DataCombine" 

	version("0.2.21", md5="a979fb7f38e7d7fd49f04c599f2efe89")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr@0.4:", type=("build", "run"))
