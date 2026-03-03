# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMiamaxent(RPackage):
	"""A Modular, Integrated Approach to Maximum Entropy Distribution
Modeling

	Tools for training, selecting, and evaluating maximum entropy
    (and standard logistic regression) distribution models. This package 
    provides tools for user-controlled transformation of explanatory variables, 
    selection of variables by nested model comparison, and flexible model 
    evaluation and projection. It follows principles based on the maximum-
    likelihood interpretation of maximum entropy modeling, and uses infinitely-
    weighted logistic regression for model fitting.
	"""
	
	homepage = "https://github.com/julienvollering/MIAmaxent"
	cran = "MIAmaxent" 

	version("1.2.0", md5="5eb4ee6d1e526be9a30e13a4fae673ac")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr@0.4.3:", type=("build", "run"))
	depends_on("r-e1071@1.6.7:", type=("build", "run"))
	depends_on("r-raster@2.5.8:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
