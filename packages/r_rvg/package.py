# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRvg(RPackage):
	"""R Graphics Devices for 'Office' Vector Graphics Output

	Vector Graphics devices for 'Microsoft PowerPoint' and 
 'Microsoft Excel'. Functions extending package 'officer' are provided to 
 embed 'DrawingML' graphics into 'Microsoft PowerPoint' presentations and 
 'Microsoft Excel' workbooks.
	"""
	
	homepage = "https://ardata-fr.github.io/officeverse/"
	cran = "rvg" 

	version("0.3.3", md5="f8d54fa6ad9124255eddb28cc30ddff2")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-officer@0.6.2:", type=("build", "run"))
	depends_on("r-gdtools", type=("build", "run"))
	depends_on("r-xml2@1:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("libpng", type=("build", "link", "run"))
