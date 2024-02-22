# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCheckdown(RPackage):
	"""Check-Fields and Check-Boxes for 'rmarkdown'

	Creates auto-grading check-fields and check-boxes for 'rmarkdown' 
    or 'quarto' HTML. It can be used in class, when teacher share materials 
    and tasks, so students can solve some problems and check their work. In 
    contrast to the 'learnr' package, the 'checkdown' package works serverlessly
    without 'shiny'.
	"""
	
	homepage = "https://agricolamz.github.io/checkdown/"
	cran = "checkdown" 

	version("0.0.12", md5="cb036aee02b1d779a1f19c3c090db1c0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-markdown", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
