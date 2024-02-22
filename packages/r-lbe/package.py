# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLbe(RPackage):
	"""Estimation of the false discovery rate.

	LBE is an efficient procedure for estimating the proportion of true null hypotheses, the false discovery rate (and so the q-values) in the framework of estimating procedures based on the marginal distribution of the p-values without assumption for the alternative hypothesis.
	"""
	
	bioc = "LBE" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/LBE_1.70.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/LBE/LBE_1.70.0.tar.gz"]

	version("1.70.0", md5="36559f365f1dbd53056e6b43bc1e06e9")

