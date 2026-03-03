# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMmrcaseselection(RPackage):
	"""Case Classification and Selection Based on Regression Results

	Researchers doing a mixed-methods analysis (nested analysis as
    developed by Lieberman (2005) <doi:10.1017/S0003055405051762>) can
    use the package for the classification of cases and case selection using
    results of a linear regression. One can designate cases 
    as typical, deviant, extreme and pathway case and use different case 
    selection strategies for the choice of a case belonging to one of
    these types.
	"""
	
	homepage = "https://github.com/ingorohlfing/MMRcaseselection"
	cran = "MMRcaseselection" 

	version("0.1.0", md5="e2e976567a50a463904aa889adf49359")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
