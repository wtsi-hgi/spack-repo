# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinyfullscreen(RPackage):
	"""Display 'HTML' Elements on Full Screen in 'Shiny' Apps

	In 'Shiny' apps, it is sometimes useful to see a plot or a
    table in full screen. Using 'Shinyfullscreen', you can easily designate
    the 'HTML' elements that can be displayed on fullscreen and use buttons to 
    trigger the fullscreen view.
	"""
	
	homepage = "https://github.com/etiennebacher/shinyfullscreen"
	cran = "shinyfullscreen" 

	version("1.1.0", md5="00864fc9463c7d3e83ef08ca7406886d")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
