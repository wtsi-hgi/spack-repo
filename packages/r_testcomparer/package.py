# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTestcomparer(RPackage):
	"""Comparing Two Diagnostic Tests with Dichotomous Results using
Paired Data

	Provides a method for comparing the results of two binary diagnostic tests using paired data. 
    Users can rapidly perform descriptive and inferential statistics in a single function call. Options permit users to select which parameters they are interested in comparing and methods for correction for multiple comparisons.
    Confidence intervals are calculated using the methods with the best coverage. Hypothesis tests use the methods with the best asymptotic performance. A summary of the methods is available in Roldán-Nofuentes (2020) <doi:10.1186/s12874-020-00988-y>.
    This package is targeted at clinical researchers who want to rapidly and effectively compare results from binary diagnostic tests.
	"""
	
	cran = "testCompareR" 

	version("1.0.2", md5="613801c020e8c727f4fa1fd0108825f8")

	depends_on("r@2.10:", type=("build", "run"))
