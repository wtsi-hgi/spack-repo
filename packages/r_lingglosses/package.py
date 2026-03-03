# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLingglosses(RPackage):
	"""Interlinear Glossed Linguistic Examples and Abbreviation Lists
Generation

	Helps to render interlinear glossed linguistic examples in html 
    'rmarkdown' documents and then semi-automatically compiles the list of
    glosses at the end of the document. It also provides a database of linguistic
    glosses.
	"""
	
	homepage = "https://CRAN.R-project.org/package=phonfieldwork"
	cran = "lingglosses" 

	version("0.0.7", md5="4a5d1ec03116f32b7ae2efa822bbe409")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
