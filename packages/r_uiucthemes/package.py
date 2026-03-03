# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUiucthemes(RPackage):
	"""'R' 'Markdown' Themes for 'UIUC' Documents and Presentations

	A set of custom 'R' 'Markdown' templates for documents and
   presentations with the University of Illinois at Urbana-Champaign (UIUC)
   color scheme and identity standards.
	"""
	
	homepage = "https://github.com/illinois-r/uiucthemes"
	cran = "uiucthemes" 

	version("0.3.1", md5="b9a44f48ef0e98477dbd3932ac0a441f")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rmarkdown@2.2:", type=("build", "run"))
	depends_on("r-xaringan@0.16:", type=("build", "run"))
