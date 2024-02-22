# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStranslate(RPackage):
	"""Simple Translation Between Different Languages

	Message translation is often managed with 'po' files and the 'gettext' programme, 
    but sometimes another solution is needed. In contrast to 'po' files, a more flexible approach 
    is used as in the Fluent <https://projectfluent.org/> project with R Markdown snippets. 
    The key-value approach allows easier handling of the translated messages.
	"""
	
	homepage = "https://github.com/sigbertklinke/stranslate"
	cran = "stranslate" 

	version("0.1.3", md5="1c0c186ccb198c4c19ff079fea3a2775")

	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
