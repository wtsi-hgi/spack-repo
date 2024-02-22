# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmdfiltr(RPackage):
	"""'Lua'-Filters for R Markdown

	A collection of 'Lua' filters that extend the functionality
  of R Markdown templates (e.g., count words or post-process citations).
	"""
	
	homepage = "https://github.com/crsh/rmdfiltr"
	cran = "rmdfiltr" 

	version("0.1.3", md5="b8be79a60575027c895637161f4d888f")

	depends_on("r-assertthat@0.2.1:", type=("build", "run"))
	depends_on("r-rmarkdown@1.12:", type=("build", "run"))
	depends_on("pandoc@2.0:", type=("build", "link", "run"))
