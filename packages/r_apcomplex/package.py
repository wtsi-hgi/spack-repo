# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RApcomplex(RPackage):
	"""Estimate protein complex membership using AP-MS protein data

	Functions to estimate a bipartite graph of protein complex membership using AP-MS data.
	"""
	
	bioc = "apComplex" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/apComplex_2.68.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/apComplex/apComplex_2.68.0.tar.gz"]

	version("2.68.0", md5="03418539dfa5904bf05f430718789fde")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-rbgl", type=("build", "run"))
	depends_on("r-rgraphviz", type=("build", "run"))
	depends_on("r-org-sc-sgd-db", type=("build", "run"))
