# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRadarchart(RPackage):
	"""Radar Chart from 'Chart.js'

	Create interactive radar charts using the 'Chart.js' 'JavaScript' library
    and the 'htmlwidgets' package. 'Chart.js' <http://www.chartjs.org/> is a 
    lightweight library that supports several types of simple chart using the 'HTML5' 
    canvas element. This package provides an R interface specifically to the 
    radar chart, sometimes called a spider chart, for visualising multivariate data.
	"""
	
	homepage = "https://github.com/mangothecat/radarchart"
	cran = "radarchart" 

	version("0.3.1", md5="100483c6c83e7873c89112cbc1c8dd6e")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
