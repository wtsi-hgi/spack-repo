# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgokabeito(RPackage):
	"""'Okabe-Ito' Scales for 'ggplot2' and 'ggraph'

	Discrete scales for the colorblind-friendly 'Okabe-Ito'
    palette, including 'color', 'fill', and 'edge_colour'. 'ggokabeito'
    provides 'ggplot2' and 'ggraph' scales to easily use the 'Okabe-Ito'
    palette in your data visualizations.
	"""
	
	homepage = "https://github.com/malcolmbarrett/ggokabeito"
	cran = "ggokabeito" 

	version("0.1.0", md5="c1b67dfd055b86f902e58fadd1882d6f")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
