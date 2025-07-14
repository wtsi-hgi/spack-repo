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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/globalSeq_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/globalSeq/globalSeq_1.30.0.tar.gz"]

    version("1.36.0", tag="RELEASE_3_21")
	version("1.30.0", sha256="e71a151ac910673542fbb47fd6c453cc00c6f21630fde9cf645ba39a399318ac")

	depends_on("r@3:", type=("build", "run"))
