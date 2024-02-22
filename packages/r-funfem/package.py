# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFunfem(RPackage):
	"""Clustering in the Discriminative Functional Subspace

	The funFEM algorithm (Bouveyron et al., 2014) allows to cluster functional data by modeling the curves within a common and discriminative functional subspace.
	"""
	
	cran = "funFEM" 

	version("1.2", md5="d0618f7a6d25da3d76c404504146d798")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-elasticnet", type=("build", "run"))
