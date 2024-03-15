# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetbiov(RPackage):
	"""A package for visualizing complex biological network

	A package that provides an effective visualization of large biological networks
	"""
	
	homepage = "http://www.bio-complexity.com"
	bioc = "netbiov" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/netbiov_1.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/netbiov/netbiov_1.36.0.tar.gz"]

	version("1.36.0", md5="4a0603ee2b7fec512349b69732218be3")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-igraph@0.7.1:", type=("build", "run"))
