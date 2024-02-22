# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnomni(RPackage):
	"""Rank Normal Transformation Omnibus Test

	Inverse normal transformation (INT) based genetic association testing. These tests are recommend for continuous traits with non-normally distributed residuals. INT-based tests robustly control the type I error in settings where standard linear regression does not, as when the residual distribution exhibits excess skew or kurtosis. Moreover, INT-based tests outperform standard linear regression in terms of power. These tests may be classified into two types. In direct INT (D-INT), the phenotype is itself transformed. In indirect INT (I-INT), phenotypic residuals are transformed. The omnibus test (O-INT) adaptively combines D-INT and I-INT into a single robust and statistically powerful approach. See McCaw ZR, Lane JM, Saxena R, Redline S, Lin X. "Operating characteristics of the rank-based inverse normal transformation for quantitative trait analysis in genome-wide association studies" <doi:10.1111/biom.13214>.
	"""
	
	cran = "RNOmni" 

	version("1.0.1.2", md5="7c3c4e4da93de11a240aad007f4c8517")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
