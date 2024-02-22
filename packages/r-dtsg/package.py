# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDtsg(RPackage):
	"""A Class for Working with Time Series Data Based on 'data.table'
and 'R6' with Largely Optional Reference Semantics

	Basic time series functionalities such as listing of missing
    values, application of arbitrary aggregation as well as rolling (asymmetric)
    window functions and automatic detection of periodicity. As it is mainly
    based on 'data.table', it is fast and (in combination with the 'R6' package)
    offers reference semantics. In addition to its native R6 interface, it
    provides an S3 interface for those who prefer the latter. Finally yet
    importantly, its functional approach allows for incorporating
    functionalities from many other packages.
	"""
	
	homepage = "https://gisler.github.io/DTSg/"
	cran = "DTSg" 

	version("1.1.3", md5="137c205b512cbd525bdb4fd92fb8e097")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
