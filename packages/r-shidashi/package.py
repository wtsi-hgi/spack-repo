# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShidashi(RPackage):
	"""A Shiny Dashboard Template System

	A template system based on 'AdminLTE3' 
    (<https://adminlte.io/themes/v3/>)
    theme. Comes with default theme that can be easily customized. 
    Developers can upload modified templates on 'Github', and users can 
    easily download templates with 'RStudio' project wizard.
    The key features of the default template include light and dark theme 
    switcher, resizing graphs, synchronizing inputs across sessions, 
    new notification system, fancy progress bars, and card-like flip 
    panels with back sides, as well as various of 'HTML' tool widgets.
	"""
	
	homepage = "https://dipterix.org/shidashi/"
	cran = "shidashi" 

	version("0.1.6", md5="ec68431fc0083367578921c7a5a19329")

	depends_on("r-digest@0.6.27:", type=("build", "run"))
	depends_on("r-fastmap@1.1:", type=("build", "run"))
	depends_on("r-formatr@1.11:", type=("build", "run"))
	depends_on("r-httr@1.4.2:", type=("build", "run"))
	depends_on("r-shiny@1.7:", type=("build", "run"))
	depends_on("r-yaml@2.2.1:", type=("build", "run"))
	depends_on("r-jsonlite@1.7.2:", type=("build", "run"))
