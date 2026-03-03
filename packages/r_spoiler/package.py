# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpoiler(RPackage):
	"""Blur 'HTML' Elements in 'Shiny' Applications Using
'Spoiler-Alert.js'

	It can be useful to temporarily hide some text or other HTML elements 
    in 'Shiny' applications. Building on 'Spoiler-Alert.js', it is possible to select the
    elements to hide at startup, to partially reveal them by hovering them, and to 
    completely show them when clicking on them.
	"""
	
	homepage = "https://github.com/etiennebacher/spoiler"
	cran = "spoiler" 

	version("1.0.0", md5="94a23a925a8e2391244c412c6cfac6aa")

	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
