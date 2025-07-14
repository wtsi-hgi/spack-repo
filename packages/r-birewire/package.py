# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBirewire(RPackage):
	"""High-performing routines for the randomization of a bipartite graph (or a binary event matrix), undirected and directed signed graph preserving degree distribution (or marginal totals)

	Fast functions for bipartite network rewiring through N consecutive switching steps (See References) and for the computation of the minimal number of switching steps to be performed in order to maximise the dissimilarity with respect to the original network. Includes functions for the analysis of the introduced randomness across the switching steps and several other routines to analyse the resulting networks and their natural projections. Extension to undirected networks and directed signed networks is also provided. Starting from version 1.9.7 a more precise bound (especially for small network) has been implemented. Starting from version 2.2.0 the analysis routine is more complete and a visual montioring of the underlying Markov Chain has been implemented. Starting from 3.6.0 the library can handle also matrices with NA (not for the directed signed graphs). Since version 3.27.1 it is possible to add a constraint for dsg generation: usually positive and negative arc between two nodes could be not accepted.
	"""
	
	homepage = "http://www.ebi.ac.uk/~iorio/BiRewire"
	bioc = "BiRewire" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/BiRewire_3.34.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/BiRewire/BiRewire_3.34.0.tar.gz"]

    version("3.40.0", tag="RELEASE_3_21")
	version("3.34.0", sha256="4d7526c04f8ad982f2b122fa91fa069f3cc5800eb33e6bc35ff7a78546abb7c0")

	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-slam", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
