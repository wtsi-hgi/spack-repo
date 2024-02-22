# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRawks(RPackage):
	"""Easily Get True-Positive Rate and False-Positive Rate and KS
Statistic

	The Kolmogorov-Smirnov (K-S) statistic is a standard method to measure the model strength for 
    credit risk scoring models. This package calculates the K–S statistic and 
    plots the true-positive rate and false-positive rate to measure the model strength. 
    This package was written with the credit marketer, who uses risk models in 
    conjunction with his campaigns. The users could read more details from 
    Thrasher (1992) <doi:10.1002/dir.4000060408> and 'pyks' <https://pypi.org/project/pyks/>.
	"""
	
	cran = "rawKS" 

	version("0.1.0", md5="a54242c4afacea4d380742f14cfed725")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
