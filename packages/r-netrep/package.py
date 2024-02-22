# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetrep(RPackage):
	"""Permutation Testing Network Module Preservation Across Datasets

	Functions for assessing the replication/preservation of a network 
  module's topology across datasets through permutation testing; Ritchie et al. 
  (2015) <doi: 10.1016/j.cels.2016.06.012>.
	"""
	
	cran = "NetRep" 

	version("1.2.7", md5="9828bbf064ce1d2c8cfa0aab019a1b39")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-rhpcblasctl", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.4:", type=("build", "run"))
