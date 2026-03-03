# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCorrfuns(RPackage):
	"""Correlation Coefficient Related Functions

	Many correlation coefficient related functions are offered, such as correlations, partial correlations and hypothesis testing using asymptotic tests and computer intensive methods (bootstrap and permutation). References include Mardia K.V., Kent J.T. and Bibby J.M. (1979). "Multivariate Analysis". ISBN: 978-0124712522. London: Academic Press.
	"""
	
	cran = "corrfuns" 

	version("1.0", md5="9c32e6b18179df43ae4066e6c6cad264")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
