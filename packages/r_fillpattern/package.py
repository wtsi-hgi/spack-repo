# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFillpattern(RPackage):
	"""Patterned Fills for 'ggplot2' and 'grid' Graphics

	Adds distinctive yet unobtrusive geometric patterns where solid 
    color fills are normally used. Patterned figures look just as 
    professional when viewed by colorblind readers or when printed in black 
    and white. The dozen included patterns can be customized in terms of scale,
    rotation, color, fill, line type, and line width. Compatible with the 
    'ggplot2' package as well as 'grid' graphics.
	"""
	
	homepage = "https://cmmr.github.io/fillpattern/"
	cran = "fillpattern" 

	version("1.0.1", md5="b11974e6008b2dfe200fde0c6cd3bf9e")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.5:", type=("build", "run"))
