# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLpgraph(RPackage):
	"""Nonparametric Smoothing of Laplacian Graph Spectra

	A nonparametric method to approximate Laplacian graph spectra of a network with 
    ordered vertices. This provides a computationally efficient algorithm for obtaining an 
	accurate and smooth estimate of the graph Laplacian basis. The approximation results can 
	then be used for tasks like change point detection, k-sample testing, and so on. The 
	primary reference is Mukhopadhyay, S. and Wang, K. (2018, Technical Report).
	"""
	
	cran = "LPGraph" 

	version("2.1", md5="6e8c47afcb94736bdd7d60214676ed47")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-pma", type=("build", "run"))
