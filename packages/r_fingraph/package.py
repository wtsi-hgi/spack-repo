# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFingraph(RPackage):
	"""Learning Graphs for Financial Markets

	Learning graphs for financial markets with optimization algorithms.
    This package contains implementations of the algorithms described in the paper:
    Cardoso JVM, Ying J, and Palomar DP (2021) <https://papers.nips.cc/paper/2021/hash/a64a034c3cb8eac64eb46ea474902797-Abstract.html>
    "Learning graphs in heavy-tailed markets", Advances in Neural Informations Processing Systems (NeurIPS).
	"""
	
	homepage = "https://github.com/convexfi/fingraph/"
	cran = "fingraph" 

	version("0.1.0", md5="229ea5c10bbd35c1ed6bf896a7eca649")

	depends_on("r-spectralgraphtopology", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
