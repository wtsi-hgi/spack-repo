# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHommel(RPackage):
	"""Methods for Closed Testing with Simes Inequality, in Particular
Hommel's Method

	Provides methods for closed testing using Simes local tests. In particular, calculates adjusted p-values for Hommel's multiple testing method, and provides lower confidence bounds for true discovery proportions. A robust but more conservative variant of the closed testing procedure that does not require the assumption of Simes inequality is also implemented. The methods have been described in detail in Goeman et al (2016) <arXiv:1611.06739v2>.
	"""
	
	cran = "hommel" 

	version("1.6", md5="f70b5b6f2d743fd52e1a2be8fcfa081d")

	depends_on("r-rcpp", type=("build", "run"))
