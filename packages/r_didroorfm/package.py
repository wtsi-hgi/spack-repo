# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDidroorfm(RPackage):
	"""Compute Recency Frequency Monetary Scores for your Customer Data

	This hosts the findRFM function which generates RFM scores on a 1-5 point scale for
             customer transaction data. The function consumes a data frame with Transaction Number,
             Customer ID, Date of Purchase (in date format) and Amount of Purchase as the attributes.
             The function returns a data frame with RFM data for the sales information.
	"""
	
	cran = "didrooRFM" 

	version("1.0.0", md5="9c2cb29dfdfb3903a37dda5870f75f79")

	depends_on("r@3.3.3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
