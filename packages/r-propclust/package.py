# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPropclust(RPackage):
	"""Propensity Clustering and Decomposition

	Implementation of propensity clustering and
        decomposition as described in Ranola et al. (2013) <doi:10.1186/1752-0509-7-21>. 
        Propensity decomposition can be viewed on the
        one hand as a generalization of the eigenvector-based
        approximation of correlation networks, and on the other hand as
        a generalization of random multigraph models and
        conformity-based decompositions.
	"""
	
	cran = "PropClust" 

	version("1.4-7", md5="203f1f11eb767a677b8820a4c3112898")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-fastcluster", type=("build", "run"))
	depends_on("r-dynamictreecut", type=("build", "run"))
