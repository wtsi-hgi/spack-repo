# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPushbar(RPackage):
	"""Create Sliders for 'Shiny'

	Create sliders from left, right, top and bottom which may include any html or 'Shiny' input or output.
	"""
	
	homepage = "https://github.com/JohnCoene/pushbar"
	cran = "pushbar" 

	version("0.1.0", md5="dc4df21a94050feaf4d1819bda7e1476")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
