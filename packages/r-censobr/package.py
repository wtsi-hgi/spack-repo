# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCensobr(RPackage):
	"""Download Data from Brazil's Population Census

	Download data from Brazil's population census. The package is built 
             on top of the 'Arrow' platform <https://arrow.apache.org/docs/r/>, 
             which allows users to work with larger-than-memory census data using 
             'dplyr' familiar functions. <https://arrow.apache.org/docs/r/articles/arrow.html#analyzing-arrow-data-with-dplyr>.
	"""
	
	homepage = "https://github.com/ipeaGIT/censobr"
	cran = "censobr" 

	version("0.3.1", md5="9d3701f5210610e5bcee0b8990750ca2")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr@1.4.1:", type=("build", "run"))
