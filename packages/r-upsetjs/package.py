# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUpsetjs(RPackage):
	"""'HTMLWidget' Wrapper of 'UpSet.js' for Exploring Large Set
Intersections

	'UpSet.js' is a re-implementation of 'UpSetR' to create interactive set visualizations for more than three sets.
  This is a 'htmlwidget' wrapper around the 'JavaScript' library 'UpSet.js'.
	"""
	
	homepage = "https://github.com/upsetjs/upsetjs_r/"
	cran = "upsetjs" 

	version("1.11.1", md5="16f0a1c4d86673eb8039227d208d95eb")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
