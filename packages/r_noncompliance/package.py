# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNoncompliance(RPackage):
	"""Causal Inference in the Presence of Treatment Noncompliance
Under the Binary Instrumental Variable Model

	A finite-population significance test of the 'sharp' causal null hypothesis that
    treatment exposure X has no effect on final outcome Y, within the principal stratum of Compliers.
    A generalized likelihood ratio test statistic is used, and the resulting p-value is exact.
    Currently, it is assumed that there are only Compliers and Never Takers in the population.
	"""
	
	homepage = "https://www.stat.washington.edu/~wloh/"
	cran = "noncompliance" 

	version("0.2.2", md5="8948a5cae2b4b6ab32c03b1005d35a6b")

	depends_on("r-data-table@1.9.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
