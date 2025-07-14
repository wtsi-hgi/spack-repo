# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGraphalignment(RPackage):
	"""GraphAlignment

	Graph alignment is an extension package for the R programming environment which provides functions for finding an alignment between two networks based on link and node similarity scores. (J. Berg and M. Laessig, "Cross-species analysis of biological networks by Bayesian alignment", PNAS 103 (29), 10967-10972 (2006))
	"""
	
	homepage = "http://www.thp.uni-koeln.de/~berg/GraphAlignment/"
	bioc = "GraphAlignment" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GraphAlignment_1.66.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GraphAlignment/GraphAlignment_1.66.0.tar.gz"]

	version("1.72.0", tag="RELEASE_3_21")
	version("1.66.0", sha256="1a446d803266504325225dab0657932018e94c954fd2121769abd4baed90513e")

