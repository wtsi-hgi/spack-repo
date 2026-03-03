# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFormattable(RPackage):
	"""Create 'Formattable' Data Structures

	Provides functions to create formattable vectors and data frames.
    'Formattable' vectors are printed with text formatting, and formattable
    data frames are printed with multiple types of formatting in HTML
    to improve the readability of data presented in tabular form rendered in
    web pages.
	"""
	
	homepage = "https://renkun-ken.github.io/formattable/"
	cran = "formattable" 

	version("0.2.1", md5="db3e9fb6605802438f9246c26da15c96")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
