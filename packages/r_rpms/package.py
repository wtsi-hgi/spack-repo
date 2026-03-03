# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpms(RPackage):
	"""Recursive Partitioning for Modeling Survey Data

	Functions to allow users to build and analyze design consistent 
    tree and random forest models using survey data from a complex sample 
    design.  The tree model algorithm can fit a linear model to survey data 
    in each node obtained by recursively partitioning the data.  The splitting 
    variables and selected splits are obtained using a randomized permutation 
    test procedure which adjusted for complex sample design features used to 
    obtain the data. Likewise the model fitting algorithm produces 
    design-consistent coefficients to any specified least squares linear model 
    between the dependent and independent variables used in the end nodes.
    The main functions return the resulting binary tree or random forest as 
    an object of "rpms" or "rpms_forest" type. The package also provides methods
    modeling a "boosted" tree or forest model and a tree model for zero-inflated
    data as well as a number of functions and methods available for use with 
    these object types.
	"""
	
	cran = "rpms" 

	version("0.5.1", md5="381422572ceab3fb2c3d3c3bce9ab785")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
