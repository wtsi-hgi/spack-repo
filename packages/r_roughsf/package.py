# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoughsf(RPackage):
	"""Visualize Spatial Data using 'roughjs'

	Draw maps using the 'javascript' library 'roughjs'. This allows to draw sketchy, hand-drawn-like maps.
	"""
	
	homepage = "https://github.com/schochastics/roughsf"
	cran = "roughsf" 

	version("1.0.0", md5="fe822f977f36c380fec35e8474e74880")

	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
