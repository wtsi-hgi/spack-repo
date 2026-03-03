# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCivis(RPackage):
	"""R Client for the 'Civis Platform API'

	A convenient interface for making
  requests directly to the 'Civis Platform API' <https://www.civisanalytics.com/platform/>.
  Full documentation available 'here' <https://civisanalytics.github.io/civis-r/>.
	"""
	
	homepage = "https://github.com/civisanalytics/civis-r"
	cran = "civis" 

	version("3.1.2", md5="24005c1824e47f25d1c3bd1319eb8372")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-future@1.8:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
