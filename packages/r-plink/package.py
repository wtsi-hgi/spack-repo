# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlink(RPackage):
	"""IRT Separate Calibration Linking Methods

	Item response theory based methods are used to compute
        linking constants and conduct chain linking of unidimensional
        or multidimensional tests for multiple groups under a common
        item design.  The unidimensional methods include the Mean/Mean,
        Mean/Sigma, Haebara, and Stocking-Lord methods for dichotomous
        (1PL, 2PL and 3PL) and/or polytomous (graded response, partial
        credit/generalized partial credit, nominal, and multiple-choice
        model) items.  The multidimensional methods include the least
        squares method and extensions of the Haebara and Stocking-Lord
        method using single or multiple dilation parameters for
        multidimensional extensions of all the unidimensional
        dichotomous and polytomous item response models.  The package
        also includes functions for importing item and/or ability
        parameters from common IRT software, conducting IRT true score
        and observed score equating, and plotting item response
        curves/surfaces, vector plots, information plots, and comparison 
        plots for examining parameter drift.
	"""
	
	cran = "plink" 

	version("1.5-1", md5="2f045240c18dbec5ccb4de47274f2113")

	depends_on("r@3.3.3:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
