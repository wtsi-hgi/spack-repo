# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRecogito(RPackage):
	"""Interactive Annotation of Text and Images

	Annotate text with entities and the relations between them. Annotate areas of interest in images with your labels. 
    Providing 'htmlwidgets' bindings to the 'recogito' <https://github.com/recogito/recogito-js> and 'annotorious' <https://github.com/recogito/annotorious> libraries.
	"""
	
	homepage = "https://github.com/DIGI-VUB/recogito"
	cran = "recogito" 

	version("0.2.1", md5="9530d6a1db8108f9e175eac5a795b597")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
