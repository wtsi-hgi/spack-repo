# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCramer(RPackage):
	"""Multivariate Nonparametric Cramer-Test for the
Two-Sample-Problem

	Provides R routine for the so called two-sample
        Cramer-Test.  This nonparametric two-sample-test on equality
        of the underlying distributions can be applied to 
        multivariate data as well as univariate data. It offers two 
        possibilities to approximate the critical value both of which 
        are included in this package.
	"""
	
	cran = "cramer" 

	version("0.9-4", md5="72feb88cb75f19b92b7149294fb45810")

	depends_on("r@0.65:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
