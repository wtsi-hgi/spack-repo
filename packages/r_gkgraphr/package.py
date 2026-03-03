# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGkgraphr(RPackage):
	"""Accessing the Official 'Google Knowledge Graph' API

	A simple way to interact with and extract data from
  the official 'Google Knowledge Graph' API <https://developers.google.com/knowledge-graph/>.
	"""
	
	homepage = "https://github.com/racorreia/gkgraphR"
	cran = "gkgraphR" 

	version("1.0.2", md5="411206277c464f684d30ab332f0b3aac")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-jsonlite@1.5:", type=("build", "run"))
	depends_on("r-httr@1.4.1:", type=("build", "run"))
	depends_on("r-isocodes@2020.3.16:", type=("build", "run"))
