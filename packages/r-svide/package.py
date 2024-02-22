# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSvide(RPackage):
	"""Functions to Ease Interactions Between R and IDE or Code Editors

	Function for the GUI API to interact with external IDE/code editors.
	"""
	
	homepage = "http://www.sciviews.org/SciViews-R"
	cran = "svIDE" 

	version("0.9-54", md5="48cd120f88f92bf9c18ef549f47eece8")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-svmisc", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
