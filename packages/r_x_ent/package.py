# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXEnt(RPackage):
	"""eXtraction of ENTity

	Provides a tool for extracting information (entities and relations between them) in text datasets. It also emphasizes the results exploration with graphical displays. It is a rule-based system and works with hand-made dictionaries and local grammars defined by users. 'x.ent' uses parsing with Perl functions and JavaScript to define user preferences through a browser and R to display and support analysis of the results extracted. Local grammars are defined and compiled with the tool Unitex, a tool developed by University Paris Est that supports multiple languages. See ?xconfig for an introduction.
	"""
	
	homepage = "https://github.com/win-stub/x.ent"
	cran = "x.ent" 

	version("1.1.7", md5="1285eca3fc9c5f81a17fb56b4a8cb75d")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("perl@5.0:", type=("build", "link", "run"))
