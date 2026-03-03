# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCopulareg(RPackage):
	"""Copula Regression

	
    Fits multivariate models in an R-vine pair copula construction framework,
    in such a way that the conditional copula can be easily evaluated.
    In addition, the package implements functionality to compute or approximate
    the conditional expectation via the conditional copula.
	"""
	
	cran = "copulareg" 

	version("0.1.0", md5="cf27a926140b9be3666588129c5b1afd")

	depends_on("r-rvinecopulib@0.5.4.1:", type=("build", "run"))
