# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReactlog(RPackage):
	"""Reactivity Visualizer for 'shiny'

	Building interactive web applications with R is incredibly easy
  with 'shiny'. Behind the scenes, 'shiny' builds a reactive graph that can
  quickly become intertwined and difficult to debug. 'reactlog'
  (Schloerke 2019) <doi:10.5281/zenodo.2591517> provides a visual insight into
  that black box of 'shiny' reactivity by constructing a directed dependency
  graph of the application's reactive state at any time point in a reactive
  recording.
	"""
	
	homepage = "https://rstudio.github.io/reactlog/"
	cran = "reactlog" 

	version("1.1.1", md5="3d89d14c074649dbe960d6bfb96952b7")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-jsonlite@0.9.16:", type=("build", "run"))
