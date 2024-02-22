# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCdata(RPackage):
	"""Fluid Data Transformations

	Supplies higher-order coordinatized data specification and fluid transform operators that include pivot and anti-pivot as special cases. 
    The methodology is describe in 'Zumel', 2018, "Fluid data reshaping with 'cdata'", <https://winvector.github.io/FluidData/FluidDataReshapingWithCdata.html> , <DOI:10.5281/zenodo.1173299> .
    This package introduces the idea of explicit control table specification of data transforms.
    Works on in-memory data or on remote data using 'rquery' and 'SQL' database interfaces.
	"""
	
	homepage = "https://github.com/WinVector/cdata/"
	cran = "cdata" 

	version("1.2.1", md5="2277690d60de6b3d68407f21246e9817")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-wrapr@2.0.9:", type=("build", "run"))
	depends_on("r-rquery@1.4.9:", type=("build", "run"))
	depends_on("r-rqdatatable@1.3.2:", type=("build", "run"))
