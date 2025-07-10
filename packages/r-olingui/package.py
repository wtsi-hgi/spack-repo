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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/OLINgui_1.76.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/OLINgui/OLINgui_1.76.0.tar.gz"]

	version("1.76.0", sha256="e7985a59139df623f1dcaa338eaa6f94f407ba31d98fd4eb31361ca2dc6b3b1e")

	depends_on("r@2:", type=("build", "run"))
	depends_on("r-olin", type=("build", "run"))
	depends_on("r-marray", type=("build", "run"))
	depends_on("r-tkwidgets", type=("build", "run"))
	depends_on("r-widgettools", type=("build", "run"))
