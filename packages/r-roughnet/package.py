# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoughnet(RPackage):
	"""Visualize Networks using 'roughjs'

	Visualize networks using the 'javascript' library 'roughjs'. This allows to draw sketchy, hand-drawn-like networks.
	"""
	
	homepage = "https://github.com/schochastics/roughnet/"
	cran = "roughnet" 

	version("1.0.1", md5="c7557b14a414ce868ba967fc1df70b63")

	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-graphlayouts", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
