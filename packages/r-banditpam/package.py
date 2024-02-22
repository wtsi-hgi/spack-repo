# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBanditpam(RPackage):
	"""Almost Linear-Time k-Medoids Clustering

	Interface to a high-performance implementation of k-medoids clustering described in Tiwari, Zhang, Mayclin, Thrun, Piech and Shomorony (2020) "BanditPAM: Almost Linear Time k-medoids Clustering via Multi-Armed Bandits" <https://proceedings.neurips.cc/paper/2020/file/73b817090081cef1bca77232f4532c5d-Paper.pdf>.
	"""
	
	cran = "banditpam" 

	version("1.0-1", md5="f8e641b5c9935ae045c409677f838849")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
