# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRhoneycomb(RPackage):
	"""Analysis of Honeycomb Selection Designs

	A useful statistical tool for the construction and analysis of Honeycomb Selection Designs. More information about this type of designs: Fasoula V. (2013) <doi:10.1002/9781118497869.ch6> Fasoula V.A., and Tokatlidis I.S. (2012) <doi:10.1007/s13593-011-0034-0> Fasoulas A.C., and Fasoula V.A. (1995) <doi:10.1002/9780470650059.ch3> Tokatlidis I. (2016) <doi:10.1017/S0014479715000150> Tokatlidis I., and Vlachostergios D. (2016)  <doi:10.3390/d8040029>.
	"""
	
	cran = "rhoneycomb" 

	version("2.3.4", md5="329774d413c0899d96a6b1b178cc82df")

	depends_on("r@4.2:", type=("build", "run"))
