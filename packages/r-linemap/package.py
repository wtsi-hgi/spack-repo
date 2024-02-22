# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLinemap(RPackage):
	"""Line Maps

	Create maps made of lines. The package contains one function:
    linemap(). linemap() displays a map made of lines using a
    raster or gridded data.
	"""
	
	homepage = "https://github.com/riatelab/linemap"
	cran = "linemap" 

	version("0.3.0", md5="2cf4807923701a65dc089bc7d3a35906")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
