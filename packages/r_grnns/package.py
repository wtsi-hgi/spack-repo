# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrnns(RPackage):
	"""General Regression Neural Networks Package

	This General Regression Neural Networks Package uses various distance functions.
     It was motivated by Specht (1991, ISBN:1045-9227), and updated from previous published paper 
     Li et al. (2016) <doi:10.1016/j.palaeo.2015.11.005>. This package includes various functions, 
     although "euclidean" distance is used traditionally.
	"""
	
	cran = "GRNNs" 

	version("0.1.0", md5="2ac562a4df351d993c985ec3fd5981db")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cvtools", type=("build", "run"))
	depends_on("r-rdist", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
