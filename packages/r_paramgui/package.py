# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RParamgui(RPackage):
	"""A Shiny GUI for some Parameter Estimation Examples

	Allows specification and fitting of some parameter estimation
    examples inspired by time-resolved spectroscopy via a Shiny GUI.
	"""
	
	homepage = "https://github.com/glotaran/paramGUI/"
	cran = "paramGUI" 

	version("2.2.0", md5="3f150af3418cf29ea24d578be837bb5e")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-timp", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
