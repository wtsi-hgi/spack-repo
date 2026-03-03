# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNglviewer(RPackage):
	"""Interactive 3D Visualization of Molecular Structures

	Provides an 'htmlwidgets' <https://www.htmlwidgets.org/> interface to 'NGL.js' <http://nglviewer.org/ngl/api/>.
    'NGLvieweR' can be used to visualize and interact with protein databank ('PDB') and structural files in R and Shiny applications.
    It includes a set of API functions to manipulate the viewer after creation in Shiny.
	"""
	
	homepage = "https://github.com/nvelden/NGLVieweR"
	cran = "NGLVieweR" 

	version("1.3.1", md5="2a1feba34b136bceca8629644ec4052c")

	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
