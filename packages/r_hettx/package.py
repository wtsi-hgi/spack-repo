# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHettx(RPackage):
	"""Fisherian and Neymanian Methods for Detecting and Measuring
Treatment Effect Variation

	Implements methods developed by Ding, Feller, and Miratrix (2016) <doi:10.1111/rssb.12124> <arXiv:1412.5000>,
    and Ding, Feller, and Miratrix (2018) <doi:10.1080/01621459.2017.1407322> <arXiv:1605.06566>
    for testing whether there is unexplained variation in treatment effects across observations, and for characterizing
    the extent of the explained and unexplained variation in treatment effects. The package includes wrapper functions
    implementing the proposed methods, as well as helper functions for analyzing and visualizing the results of the test.
	"""
	
	cran = "hettx" 

	version("0.1.3", md5="39753d5d4d6d3dd61b640b5a61ab975f")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-formula-tools", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
