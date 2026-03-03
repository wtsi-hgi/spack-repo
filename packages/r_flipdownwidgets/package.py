# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlipdownwidgets(RPackage):
	"""A Wrapper of JavaScript Library 'flipdown.js'

	Include a countdown <https://github.com/PButcher/flipdown> in all R contexts with the convenience of 'htmlwidgets'.
	"""
	
	homepage = "https://github.com/fanggong/flipdownWidgets"
	cran = "flipdownWidgets" 

	version("0.1.0", md5="7f8fbfbdf637e92dc89e27b1d40f59ab")

	depends_on("r-htmlwidgets", type=("build", "run"))
