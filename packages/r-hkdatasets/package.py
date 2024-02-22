# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHkdatasets(RPackage):
	"""Datasets Related to Hong Kong

	Datasets related to Hong Kong, including information on the 2019 elected District Councillors (<https://www.districtcouncils.gov.hk> and <https://dce2019.hk01.com/>) and traffic collision data from the Hong Kong Department of Transport (<https://www.td.gov.hk/>). All
    of the data in this package is available in the public domain.
	"""
	
	homepage = "https://hong-kong-districts-info.github.io/hkdatasets/"
	cran = "hkdatasets" 

	version("1.0.0", md5="9e5bbe62ce33209009d29cc934bf373a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-fst", type=("build", "run"))
