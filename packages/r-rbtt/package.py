# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbtt(RPackage):
	"""Alternative Bootstrap-Based t-Test Aiming to Reduce Type-I Error
for Non-Negative, Zero-Inflated Data

	Tu & Zhou (1999) <doi:10.1002/(SICI)1097-0258(19991030)18:20%3C2749::AID-SIM195%3E3.0.CO;2-C> showed that comparing the means of populations whose data-generating distributions are non-negative with excess zero observations is a problem of great importance in the analysis of medical cost data. In the same study, Tu & Zhou discuss that it can be difficult to control type-I error rates of general-purpose statistical tests for comparing the means of these particular data sets. This package allows users to perform a modified bootstrap-based t-test that aims to better control type-I error rates in these situations.
	"""
	
	cran = "rbtt" 

	version("0.1.0", md5="daf97a27d3e54cd236a29f7fac67c19d")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
