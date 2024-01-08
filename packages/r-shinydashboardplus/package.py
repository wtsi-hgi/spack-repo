# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class RShinydashboardplus(RPackage):
	"""Add More 'AdminLTE2' Components to 'shinydashboard'

	Extend 'shinydashboard' with 'AdminLTE2' components. 
             'AdminLTE2' is a free 'Bootstrap 3' dashboard template available
             at <https://adminlte.io>. Customize boxes, add timelines and a lot more. 
	"""
	
	homepage = "https://github.com/RinteRface/shinydashboardPlus"
	cran = "shinydashboardPlus" 

	version("2.0.3", md5="a5f4b958261c0fe49abd1a8491fbbbdb")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-fresh", type=("build", "run"))
	depends_on("r-waiter@0.2.3:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
