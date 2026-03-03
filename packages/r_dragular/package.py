# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDragular(RPackage):
	"""Drag and Drop Elements in 'Shiny' using 'Dragula Javascript
Library'

	Move elements between containers in 'Shiny' without explicitly using 'JavaScript'. It can be used to build custom inputs or to change the positions of user interface elements like plots or tables.
	"""
	
	homepage = "https://dragular.zstat.pl/"
	cran = "dragulaR" 

	version("0.3.1", md5="41c42423dbdda6e14586ae891e1dfb70")

	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
