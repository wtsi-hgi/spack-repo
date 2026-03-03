# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDesigner(RPackage):
	"""'Shiny' UI Prototype Builder

	A 'shiny' application that enables the user to create a
    prototype UI, being able to drag and drop UI components before being
    able to save or download the equivalent R code.
	"""
	
	homepage = "https://ashbaldry.github.io/designer/"
	cran = "designer" 

	version("0.3.0", md5="3128a6c50e92ac616319f00d1c26e4a6")

	depends_on("r-bs4dash", type=("build", "run"))
	depends_on("r-bslib", type=("build", "run"))
	depends_on("r-cicerone", type=("build", "run"))
	depends_on("r-config@0.3.1:", type=("build", "run"))
	depends_on("r-fontawesome", type=("build", "run"))
	depends_on("r-golem@0.3.1:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-shinipsum", type=("build", "run"))
	depends_on("r-shiny@1.7.1:", type=("build", "run"))
	depends_on("r-shinyscreenshot", type=("build", "run"))
