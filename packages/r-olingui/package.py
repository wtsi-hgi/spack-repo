# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROlingui(RPackage):
	"""Graphical user interface for OLIN

	Graphical user interface for the OLIN package
	"""
	
	homepage = "http://olin.sysbiolab.eu"
	bioc = "OLINgui"

	version("1.82.0", commit="6d53023c0e790449453c369b7d6ac481dc5e5b62")
	version("1.76.0", commit="f7be69d829b748bb52dac3c310b552a543cae18e")

	depends_on("r@2:", type=("build", "run"))
	depends_on("r-olin", type=("build", "run"))
	depends_on("r-marray", type=("build", "run"))
	depends_on("r-tkwidgets", type=("build", "run"))
	depends_on("r-widgettools", type=("build", "run"))
