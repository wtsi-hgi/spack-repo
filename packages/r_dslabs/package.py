# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDslabs(RPackage):
	"""Data Science Labs

	Datasets and functions that can be used for data analysis practice, homework and projects in data science courses and workshops. 26 datasets are available for case studies in data visualization, statistical inference, modeling, linear regression, data wrangling and machine learning.
	"""
	
	cran = "dslabs" 

	version("0.8.0", md5="31824b3df1dc07ba34e838ff97172ebb")
	version("0.7.6", md5="be10796eee7eba6d4818b6557e7f7fb2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
