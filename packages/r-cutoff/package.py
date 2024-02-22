# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCutoff(RPackage):
	"""Seek the Significant Cutoff Value

	Seek the significant cutoff value for a continuous variable, which will 
    be transformed into a classification, for linear regression, 
    logistic regression, logrank analysis and cox regression. First of all, 
    all combinations will be gotten by combn() function. Then n.per argument, 
    abbreviated of total number percentage, will be used to remove the combination 
    of smaller data group. In logistic, Cox regression and logrank analysis, 
    we will also use p.per argument, patient percentage, to filter the lower 
    proportion of patients in each group. Finally, p value in regression 
    results will be used to get the significant combinations and output 
    relevant parameters. In this package, there is no limit to the number of 
    cutoff points, which can be 1, 2, 3 or more. Still, we provide 2 methods, 
    typical Bonferroni and Duglas G (1994) <doi: 10.1093/jnci/86.11.829>, to 
    adjust the p value, Missing values will be deleted by na.omit() function 
    before analysis.
	"""
	
	homepage = "https://github.com/yikeshu0611/cutoff"
	cran = "cutoff" 

	version("1.3", md5="fb586c80f7f17d77b0571649402fc530")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-set", type=("build", "run"))
	depends_on("r-do", type=("build", "run"))
	depends_on("r-rocit", type=("build", "run"))
