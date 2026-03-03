# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPosterdown(RPackage):
	"""Generate PDF Conference Posters Using R Markdown

	Use 'rmarkdown' and 'pagedown' to generate
    HTML and PDF conference posters.
	"""
	
	homepage = "https://github.com/brentthorne/posterdown"
	cran = "posterdown" 

	version("1.0", md5="aee65183ed15bd9c45d0be0c2a7d424a")

	depends_on("r-pagedown", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
