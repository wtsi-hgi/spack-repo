# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlobalseq(RPackage):
	"""Global Test for Counts

	The method may be conceptualised as a test of overall significance in regression analysis, where the response variable is overdispersed and the number of explanatory variables exceeds the sample size. Useful for testing for association between RNA-Seq and high-dimensional data.
	"""
	
	homepage = "https://github.com/rauschenberger/globalSeq"
	bioc = "globalSeq"

	version("1.36.0", commit="c07d19fd4b362f4d60f8c6382d421a0aff905c96")
	version("1.30.0", commit="3915a871dd80d5d896bb479209aabcbe15f30c9e")

	depends_on("r@3:", type=("build", "run"))
