# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRandomcolor(RPackage):
	"""Generate Attractive Random Colors

	Simple methods to generate attractive random colors. The random
  colors are from a wrapper of 'randomColor.js'
  <https://github.com/davidmerfield/randomColor>. In addition, it also generates
  optimally distinct colors based on k-means (inspired by 'IWantHue'
  <https://github.com/medialab/iwanthue>).
	"""
	
	cran = "randomcoloR" 

	version("1.1.0.1", md5="e01cf5290282d7d8c7ce69979ecd6316")

	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-v8", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
