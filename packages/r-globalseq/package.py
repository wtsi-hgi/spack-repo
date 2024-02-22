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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/globalSeq_1.30.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/globalSeq/globalSeq_1.30.0.tar.gz"]

	version("1.30.0", md5="1b427214cf1345b8d75ba69dc02adb77")

	depends_on("r@3:", type=("build", "run"))
