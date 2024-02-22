# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVarrank(RPackage):
	"""Heuristics Tools Based on Mutual Information for Variable
Ranking

	A computational toolbox of heuristics approaches for performing variable ranking and feature selection based on mutual information well adapted for multivariate system epidemiology datasets. The core function is a general implementation of the minimum redundancy maximum relevance model. R. Battiti (1994) <doi:10.1109/72.298224>. Continuous variables are discretized using a large choice of rule. Variables ranking can be learned with a sequential forward/backward search algorithm. The two main problems that can be addressed by this package is the selection of the most representative variable within a group of variables of interest (i.e. dimension reduction) and variable ranking with respect to a set of features of interest. 
	"""
	
	homepage = "https://www.math.uzh.ch/pages/varrank/"
	cran = "varrank" 

	version("0.5", md5="5813663ce3af9a150365eb2a75e6cb52")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
