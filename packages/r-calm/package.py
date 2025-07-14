# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCalm(RPackage):
	"""Covariate Assisted Large-scale Multiple testing

	Statistical methods for multiple testing with covariate information. Traditional multiple testing methods only consider a list of test statistics, such as p-values. Our methods incorporate the auxiliary information, such as the lengths of gene coding regions or the minor allele frequencies of SNPs, to improve power.
	"""
	
	bioc = "calm"

	version("1.22.0", commit="ab940441b3bf46aeae7d5df06c085ea8641453bb")
	version("1.16.0", commit="1cc42b5276c2782e7cd35b652bd81df5949d8039")

	depends_on("r-mgcv", type=("build", "run"))
