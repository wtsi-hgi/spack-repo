# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlfma(RPackage):
	"""A GUI to View, Design and Export Various Graphs of Data

	Provides a graphical user interface for viewing and designing various types of graphs of the data. The graphs can be saved in different formats of an image.
	"""
	
	cran = "plfMA" 

	version("2.0", md5="6b22ad54d9ac978be6f738cac86365d3")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-gwidgets2", type=("build", "run"))
	depends_on("r-gwidgets2tcltk", type=("build", "run"))
	depends_on("r-tkrplot", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
