# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RThorn(RPackage):
	"""'HTMLwidgets' Displaying Some 'WebGL' Shaders

	Creates some 'WebGL' shaders. They can be used as the background of a 'Shiny' app. They also can be visualized in the 'RStudio' viewer pane or included in 'Rmd' documents, but this is pretty useless, besides contemplating them.
	"""
	
	homepage = "https://github.com/stla/thorn"
	cran = "thorn" 

	version("0.2.0", md5="fcd69f04ffd768709a78cc8e91f8e648")

	depends_on("r-htmlwidgets", type=("build", "run"))
