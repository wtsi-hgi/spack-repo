# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFuzzydbscan(RPackage):
	"""Run and Predict a Fuzzy DBScan

	
    An interface for training Fuzzy DBScan with both Fuzzy Core and Fuzzy Border.
    Therefore, the package provides a method to initialize and run the algorithm and a
    function to predict new data w.t.h. of 'R6'.
    The package is build upon the paper "Fuzzy Extensions of the DBScan algorithm"
    from Ienco and Bordogna (2018) <doi:10.1007/s00500-016-2435-0>.
    A predict function assigns new data according to the same criteria as the algorithm itself.
    However, the prediction function freezes the algorithm to preserve the trained
    cluster structure and treats each new prediction object individually.
	"""
	
	cran = "FuzzyDBScan" 

	version("0.0.3", md5="24935e786bc8660b858c3666adc3b010")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dbscan", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
