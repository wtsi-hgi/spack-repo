# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAde4tkgui(RPackage):
	"""'ade4' Tcl/Tk Graphical User Interface

	A Tcl/Tk GUI for some basic functions in the 'ade4' package.
	"""
	
	homepage = "http://pbil.univ-lyon1.fr/ade4TkGUI/"
	cran = "ade4TkGUI" 

	version("0.3-1", md5="688218d286d6912dd67d3ed7ee378202")

	depends_on("r-ade4@1.4.3:", type=("build", "run"))
	depends_on("r-adegraphics", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
