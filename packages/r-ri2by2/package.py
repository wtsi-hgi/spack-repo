# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRi2by2(RPackage):
	"""Randomization Inference for Treatment Effects on a Binary
Outcome

	Computes attributable effects based confidence interval, permutation test confidence interval, or asymptotic confidence interval for the average treatment effect on a binary outcome. Methods outlined in further detail in Rigdon and Hudgens (2015) <doi:10.1002/sim.6384>. 
	"""
	
	cran = "RI2by2" 

	version("1.4", md5="9c2739d5a8c7e381515e971eb0ef2be5", url="https://cran.r-project.org/src/contrib/RI2by2_1.4.tar.gz")

	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
