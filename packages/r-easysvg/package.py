# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REasysvg(RPackage):
	"""An Easy SVG Basic Elements Generator

	This SVG elements generator can easily generate 
    SVG elements such as rect, line, circle, ellipse, polygon, 
    polyline, text and group. Also, it can combine and 
    output SVG elements into a SVG file.
	"""
	
	homepage = "https://github.com/ytdai/easySVG"
	cran = "easySVG" 

	version("0.1.0", md5="c6eaaf08e9d3b9855bf440b9ce5067e9")

	depends_on("r@3.3:", type=("build", "run"))
