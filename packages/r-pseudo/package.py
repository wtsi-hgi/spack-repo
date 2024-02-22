# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPseudo(RPackage):
	"""Computes Pseudo-Observations for Modeling

	Various functions for computing pseudo-observations for censored data regression. Computes pseudo-observations for modeling: competing risks based on the cumulative incidence function, survival function based on the restricted mean,  survival function based on the Kaplan-Meier estimator see Klein et al. (2008) <doi:10.1016/j.cmpb.2007.11.017>. 
	"""
	
	cran = "pseudo" 

	version("1.4.3", md5="12a3cd61fa5d73d526ac6f5567ae2e61")

	depends_on("r@3.3.3:", type=("build", "run"))
	depends_on("r-kmsurv", type=("build", "run"))
	depends_on("r-geepack", type=("build", "run"))
