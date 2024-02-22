# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSsddata(RPackage):
	"""Species Sensitivity Distribution Data

	Reference data sets of species sensitivities to compare the 
    results of fitting species sensitivity distributions 
    using software such as 'ssdtools' and 'Burrlioz'. 
    It consists of 17 primary data sets from
    four different Australian and Canadian organizations as well as five
    datasets from anonymous sources. It also includes a data set of the
    results of fitting various distributions using different software.
	"""
	
	cran = "ssddata" 

	version("1.0.0", md5="17dbb32d134bea0e9072f2201e14e879")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-chk", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
