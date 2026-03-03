# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcartocolor(RPackage):
	"""'CARTOColors' Palettes

	Provides color schemes for maps and other graphics
    designed by 'CARTO' as described at <https://carto.com/carto-colors/>.
    It includes four types of palettes: aggregation, diverging, qualitative, 
    and quantitative.
	"""
	
	homepage = "https://github.com/Nowosad/rcartocolor"
	cran = "rcartocolor" 

	version("2.1.1", md5="ffd01ddbc482fa667cd74544deec11d0")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
