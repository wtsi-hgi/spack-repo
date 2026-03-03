# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastcmh(RPackage):
	"""Significant Interval Discovery with Categorical Covariates

	A method which uses the Cochran-Mantel-Haenszel test with significant pattern mining to detect intervals in binary genotype data which are significantly associated with a particular phenotype, while accounting for categorical covariates.
	"""
	
	cran = "fastcmh" 

	version("0.2.7", md5="48c8799884604a663faa8c4c81fdeb8e")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-bindata", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
