# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinyselect(RPackage):
	"""A Wrapper of the 'react-select' Library

	Provides a select control widget for 'Shiny'. It is easily
    customizable, and one can easily use HTML in the items and KaTeX to
    type mathematics.
	"""
	
	homepage = "https://github.com/stla/shinySelect"
	cran = "shinySelect" 

	version("1.3.0", md5="ef8aeb7e827dc204877ea792fb862481")

	depends_on("r-fontawesome", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-reactr", type=("build", "run"))
