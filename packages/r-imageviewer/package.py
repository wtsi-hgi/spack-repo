# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImageviewer(RPackage):
	"""Simple 'htmlwidgets' Image Viewer with WebGL Brightness/Contrast

	Display a 2D-matrix data as a interactive zoomable gray-scale image viewer, providing tools for manual data inspection. The viewer window shows cursor guiding lines and a corresponding data slices for both axes at the current cursor position. A tool-bar allows adjusting image display brightness/contrast through WebGL filters and performing basic high-pass/low-pass filtering.
	"""
	
	homepage = "https://github.com/yapus/imageviewer"
	cran = "imageviewer" 

	version("0.1.0", md5="c82587ee7645d04fc1bbeb9cdd3f9d1e")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
