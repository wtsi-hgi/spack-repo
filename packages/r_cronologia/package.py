# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCronologia(RPackage):
	"""Create an HTML Vertical Timeline from a Data Frame in
'rmarkdown' and 'shiny'

	Creates an HTML vertical timeline from a data frame as an input for
    'rmarkdown' documents and 'shiny' applications.
	"""
	
	homepage = "https://github.com/feddelegrand7/cronologia"
	cran = "cronologia" 

	version("0.2.0", md5="78809e50c33b8e4da3ab6c94dfdfb95e")

	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
