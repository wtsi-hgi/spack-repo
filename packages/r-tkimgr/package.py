# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTkimgr(RPackage):
	"""Simple Image Viewer for R Using the 'tcltk' Package

	A 'Tcl/Tk' Graphical User Interface (GUI) to display images than can be zoomed and panned using the mouse and keyboard shortcuts. 'tkImgR' read and write different image formats (PPM/PGM, PNG and GIF) using the standard 'Tcl/Tk' distribution (>=8.6), but other formats (JPEG, TIFF, CR2) can be handled using the 'tkImg' package for 'Tcl/Tk'.
	"""
	
	cran = "tkImgR" 

	version("0.0.5", md5="ddb62428d81cdb8c8238f7ff669a84e2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-tkrplotr", type=("build", "run"))
	depends_on("tcl@8.6:", type=("build", "link", "run"))
	depends_on("tk@8.6:", type=("build", "link", "run"))
