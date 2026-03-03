# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVuer(RPackage):
	"""'Vuejs' Helpers and 'Htmlwidget'

	Make it easy to use 'vue' in R with helper
              dependency functions and examples.
	"""
	
	homepage = "https://github.com/vue-r/vueR"
	cran = "vueR" 

	version("0.6.0", md5="8ac27e6578de757bb3341bd4fc0e6111")

	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-htmlwidgets@0.6:", type=("build", "run"))
