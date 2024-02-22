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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/calm_1.16.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/calm/calm_1.16.0.tar.gz"]

	version("1.16.0", md5="9a2b4c48021193636c88c997331ede2d")

	depends_on("r-mgcv", type=("build", "run"))
