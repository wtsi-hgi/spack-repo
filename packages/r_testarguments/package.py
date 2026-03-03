# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTestarguments(RPackage):
	"""Test (Multiple) Arguments of a User-Defined Prediction Algorithm

	Finding the best values for user-specified arguments of a prediction algorithm can be difficult, particularly if there is an interaction between argument levels. This package automates the testing of any user-defined prediction algorithm over an arbitrary number of arguments. It includes functions for testing the algorithm over the given arguments with respect to an arbitrary number of user-defined diagnostics, visualising the results of these tests, and finding the optimal argument combinations with respect to each diagnostic.
	"""
	
	cran = "testarguments" 

	version("0.0.1", md5="aafbaa9bfe3b18279f46dc83ce649cf0")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
