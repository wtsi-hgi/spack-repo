# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGraphframes(RPackage):
	"""Interface for 'GraphFrames'

	A 'sparklyr' <https://spark.rstudio.com/> extension that provides an R 
  interface for 'GraphFrames' <https://graphframes.github.io/>. 'GraphFrames' is a package
  for 'Apache Spark' that provides a DataFrame-based API for working with graphs. Functionality
  includes motif finding and common graph algorithms, such as PageRank and Breadth-first
  search.
	"""
	
	homepage = "https://github.com/rstudio/graphframes"
	cran = "graphframes" 

	version("0.1.2", md5="17b616a87fa113f1fde22adf9264e80c")

	depends_on("r-sparklyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-forge", type=("build", "run"))
