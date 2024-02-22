# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimplefdr(RPackage):
	"""Simple False Discovery Rate Calculation

	Using the adjustment method from Benjamini & Hochberg (1995) <doi:10.1111/j.2517-6161.1995.tb02031.x>, this package determines which variables are significant under repeated testing with a given dataframe of p values and an user defined "q" threshold.  It then returns the original dataframe along with a significance column where an asterisk denotes a significant p value after FDR calculation, and NA denotes all other p values. This package uses the Benjamini & Hochberg method specifically as described in Lee, S., & Lee, D. K. (2018) <doi:10.4097/kja.d.18.00242>. 
	"""
	
	cran = "simpleFDR" 

	version("1.1", md5="a8970f63f4813cb665f583364a3e9a23")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
