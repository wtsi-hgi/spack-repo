# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSvdialogstcltk(RPackage):
	"""'SciViews' - Standard Dialog Boxes using Tcl/Tk

	Reimplementation of the 'svDialogs' dialog boxes in Tcl/Tk.
	"""
	
	homepage = "https://github.com/SciViews/svDialogstcltk"
	cran = "svDialogstcltk" 

	version("1.0.0", md5="8809cf518c9fca0eea5bc73498787667")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-svdialogs@1:", type=("build", "run"))
	depends_on("r-svgui@1:", type=("build", "run"))
