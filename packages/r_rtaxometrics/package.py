# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtaxometrics(RPackage):
	"""Taxometric Analysis

	We provide functions to perform taxometric analyses. This package contains 46 functions, but only 5 should be called directly by users. CheckData() should be run prior to any taxometric analysis to ensure that the data are appropriate for taxometric analysis. RunTaxometrics() performs taxometric analyses for a sample of data. RunCCFIProfile() performs a series of taxometric analyses to generate a CCFI profile. CreateData() generates a sample of categorical or dimensional data. ClassifyCases() assigns cases to groups using the base-rate classification method.
	"""
	
	cran = "RTaxometrics" 

	version("3.2.1", md5="83c18c99ce0c1b901f0c2b8a9ce17dc5")

