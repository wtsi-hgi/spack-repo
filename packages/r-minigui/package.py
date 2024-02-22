# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMinigui(RPackage):
	"""Tcl/Tk Quick and Simple Function GUI

	Quick and simple Tcl/Tk Graphical User Interface 
  to call functions. Also comprises a very simple experimental 
  GUI framework.
	"""
	
	cran = "miniGUI" 

	version("0.8-1", md5="1829cbccd2231e009419bdf5e74c76e1")

	depends_on("r@2.5:", type=("build", "run"))
