# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBs4dash(RPackage):
	"""A 'Bootstrap 4' Version of 'shinydashboard'

	Make 'Bootstrap 4' Shiny dashboards. Use the full power
    of 'AdminLTE3', a dashboard template built on top of 'Bootstrap 4' 
    <https://github.com/ColorlibHQ/AdminLTE>.
	"""
	
	homepage = "https://rinterface.github.io/bs4Dash/index.html"
	cran = "bs4Dash" 

	version("2.3.3", md5="a7b3aa28533c2c9562e053f12d197b15")

	depends_on("r-shiny@1.6:", type=("build", "run"))
	depends_on("r-htmltools@0.5.1.1:", type=("build", "run"))
	depends_on("r-jsonlite@0.9.16:", type=("build", "run"))
	depends_on("r-fresh", type=("build", "run"))
	depends_on("r-waiter@0.2.3:", type=("build", "run"))
	depends_on("r-httpuv@1.5.2:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-bslib@0.2.4:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
