# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparkline(RPackage):
	"""'jQuery' Sparkline 'htmlwidget'

	Include interactive sparkline charts
    <http://omnipotent.net/jquery.sparkline> in 
    all R contexts with the convenience of 'htmlwidgets'.  
	"""
	
	cran = "sparkline" 

	version("2.0", md5="46e07b1c3972f18233e0325c95368a7f")

	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-htmlwidgets@0.8:", type=("build", "run"))
