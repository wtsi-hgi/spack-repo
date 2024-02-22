# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastjt(RPackage):
	"""Efficient Jonckheere-Terpstra Test Statistics

	This 'Rcpp'-based package implements highly efficient functions for the calculation of the Jonckheere-Terpstra statistic. It can be used for a variety of applications, including feature selection in machine learning problems, or to conduct genome-wide association studies (GWAS) with multiple quantitative phenotypes. The code leverages 'OpenMP' directives for multi-core computing to reduce overall processing time. 
	"""
	
	cran = "fastJT" 

	version("1.0.6", md5="e29bbdb24f5abb83a15a4d294fa1bd96")

	depends_on("r-rcpp", type=("build", "run"))
