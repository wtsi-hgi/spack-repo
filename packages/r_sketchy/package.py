# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSketchy(RPackage):
	"""Create Custom Research Compendiums

	Provides functions to create and manage research compendiums for data analysis. Research compendiums are a standard and intuitive folder structure for organizing the digital materials of a research project, which can significantly improve reproducibility. The package offers several compendium structure options that fit different research project as well as the ability of duplicating the folder structure of existing projects or implementing custom structures. It also simplifies the use of version control.
	"""
	
	homepage = "https://github.com/maRce10/sketchy"
	cran = "sketchy" 

	version("1.0.2", md5="3c13c290b0ab1c66f05a43d69746f94a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-packrat", type=("build", "run"))
	depends_on("r-git2r", type=("build", "run"))
