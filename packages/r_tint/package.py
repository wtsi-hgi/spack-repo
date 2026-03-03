# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTint(RPackage):
	"""'tint' is not 'Tufte'

	A 'tufte'-alike style for 'rmarkdown'.
 A modern take on the 'Tufte' design for pdf and html vignettes,
 building on the 'tufte' package with additional contributions
 from the 'knitr' and 'ggtufte' package, and also acknowledging
 the key influence of 'envisioned css'.
	"""
	
	homepage = "https://github.com/eddelbuettel/tint/"
	cran = "tint" 

	version("0.1.4", md5="02719e7f84fdf1a30ef2237b04f525b6")

	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
