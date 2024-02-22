# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetablue(RPackage):
	"""BLUE for Combining Location and Scale Information in a
Meta-Analysis

	The sample mean and standard deviation are two commonly used statistics in meta-analyses, 
    but some trials use other summary statistics such as the median and quartiles to report the results. 
    Therefore, researchers need to transform those information back to the sample mean and 
    standard deviation. This package implemented sample mean estimators by Luo et al. (2016) <arXiv:1505.05687>, sample standard deviation estimators by Wan et al. (2014) <arXiv:1407.8038>, and the best linear unbiased estimators (BLUEs) of location and scale parameters by Yang et al. (2018, submitted) based on sample quantiles derived summaries in a meta-analysis.
	"""
	
	cran = "metaBLUE" 

	version("1.0.0", md5="23acf3220e15edc0fed518bd682d431b")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
