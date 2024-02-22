# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWosr(RPackage):
	"""Clients to the 'Web of Science' and 'InCites' APIs

	R clients to the 'Web of Science' and 'InCites' 
  <https://clarivate.com/products/data-integration/> APIs, which 
  allow you to programmatically download publication and citation data
  indexed in the 'Web of Science' and 'InCites' databases.
	"""
	
	homepage = "https://vt-arc.github.io/wosr/index.html"
	cran = "wosr" 

	version("0.3.0", md5="c56dffb850e299cae6acc2679c23a72a")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
