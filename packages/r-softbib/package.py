# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSoftbib(RPackage):
	"""Software Bibliographies for R Projects

	Detect libraries used in a project and automatically create software bibliographies in 'PDF', 'Word', 'Rmarkdown', and 'BibTeX' formats.
	"""
	
	homepage = "https://github.com/vincentarelbundock/softbib"
	cran = "softbib" 

	version("0.0.2", md5="32e304d50bab2b6b396bca605f684665")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-renv", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-bibtex", type=("build", "run"))
