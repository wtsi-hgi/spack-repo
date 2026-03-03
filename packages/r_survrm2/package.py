# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvrm2(RPackage):
	"""Comparing Restricted Mean Survival Time

	Performs two-sample comparisons using the restricted mean survival time (RMST) as a summary measure of the survival time distribution. Three kinds of between-group contrast metrics (i.e., the difference in RMST, the ratio of RMST and the ratio of the restricted mean time lost (RMTL)) are computed. It performs an ANCOVA-type covariate adjustment as well as unadjusted analyses for those measures. 
	"""
	
	cran = "survRM2" 

	version("1.0-4", md5="fb69c323518573e676ad1a1603b00111", url="https://cran.r-project.org/src/contrib/survRM2_1.0-4.tar.gz")

	depends_on("r-survival", type=("build", "run"))
