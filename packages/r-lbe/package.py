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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/LBE_1.70.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/LBE/LBE_1.70.0.tar.gz"]

    version("1.76.0", tag="RELEASE_3_21")
	version("1.70.0", sha256="99990d21cff0a2b427afbade12547c637c5aeb63a494f956b6d6f0d97a7e723b")

