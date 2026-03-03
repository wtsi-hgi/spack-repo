# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBondvaluation(RPackage):
	"""Fixed Coupon Bond Valuation Allowing for Odd Coupon Periods and
Various Day Count Conventions

	Analysis of large datasets of fixed coupon bonds, allowing for irregular first and last coupon periods and various day count conventions. With this package you can compute the yield to maturity, the modified and MacAulay durations and the convexity of fixed-rate bonds. It provides the function AnnivDates, which can be used to evaluate the quality of the data and return time-invariant properties and temporal structure of a bond.
	"""
	
	cran = "BondValuation" 

	version("0.1.1", md5="228a935552410b4f5fc1394ae66b875a")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-timedate", type=("build", "run"))
