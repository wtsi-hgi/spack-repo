# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultiness(RPackage):
	"""MULTIplex NEtworks with Shared Structure

	Model fitting and simulation for Gaussian and logistic inner 
    product MultiNeSS models for multiplex networks. The package implements 
    a convex fitting algorithm with fully adaptive parameter tuning, 
    including options for edge cross-validation. For more details see 
    MacDonald et al. (2020).  
	"""
	
	homepage = "https://github.com/peterwmacd/multiness/"
	cran = "multiness" 

	version("1.0.2", md5="41bb562eb94af5d56a317ed95abea1a4")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-glmnet@4.0.2:", type=("build", "run"))
	depends_on("r-matrix@1.1:", type=("build", "run"))
	depends_on("r-rspectra@0.16:", type=("build", "run"))
