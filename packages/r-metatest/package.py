# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetatest(RPackage):
	"""Fit and Test Metaregression Models

	Fits and tests meta regression models and generates a
 number of useful test statistics: next to t- and z-tests, the likelihood ratio,
 bartlett corrected likelihood ratio and permutation tests are performed on
 the model coefficients.
	"""
	
	cran = "metatest" 

	version("1.0-5", md5="5a8e46fa5f7cbed7c240b91ed0aa3212")

	depends_on("r@3.5:", type=("build", "run"))
