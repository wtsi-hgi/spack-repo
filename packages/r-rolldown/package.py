# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRolldown(RPackage):
	"""R Markdown Output Formats for Storytelling

	R Markdown output formats based on JavaScript libraries such as
    'Scrollama' (<https://github.com/russellgoldenberg/scrollama>) for storytelling.
	"""
	
	cran = "rolldown" 

	version("0.1", md5="6fb786e25bbad225388a6d5fcca183d6")

	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-bookdown", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
