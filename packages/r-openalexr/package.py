# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpenalexr(RPackage):
	"""Getting Bibliographic Records from 'OpenAlex' Database Using
'DSL' API

	A set of tools to extract bibliographic content from
    'OpenAlex' database using API <https://docs.openalex.org>.
	"""
	
	homepage = "https://github.com/ropensci/openalexR"
	cran = "openalexR" 

	version("1.2.3", md5="8d06b3b03db96263213f80c7ee19f8b7")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
