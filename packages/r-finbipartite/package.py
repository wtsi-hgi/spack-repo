# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFinbipartite(RPackage):
	"""Learning Bipartite Graphs: Heavy Tails and Multiple Components

	Learning bipartite and k-component bipartite graphs from financial
     datasets. This package contains implementations of the algorithms described
     in the paper: Cardoso JVM, Ying J, and Palomar DP (2022).
     <https://openreview.net/pdf?id=WNSyF9qZaMd>
     "Learning bipartite graphs: heavy tails and multiple components,
     Advances in Neural Informations Processing Systems" (NeurIPS).
	"""
	
	homepage = "https://github.com/convexfi/bipartite/"
	cran = "finbipartite" 

	version("0.1.0", md5="45b50fcc17596b51a13d16a7fac391d6")

	depends_on("r-spectralgraphtopology", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-cvxr", type=("build", "run"))
