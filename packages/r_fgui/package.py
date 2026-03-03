# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFgui(RPackage):
	"""Function GUI

	Rapidly create a GUI interface for a function you created by automatically creating widgets for arguments of the function. Automatically parses help routines for context-sensitive help to these arguments. The interface essentially a wrapper to some Tcl/Tk routines to both simplify and facilitate GUI creation. More advanced Tcl/Tk routines/GUI objects can be incorporated into the interface for greater customization for the more experienced.
	"""
	
	homepage = "https://sites.google.com/site/thomashoffmannproject/software/fgui"
	cran = "fgui" 

	version("1.0-8", md5="a83dd8acdd54766b070a82001cbf7cae")

