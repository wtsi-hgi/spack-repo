# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCodatags(RPackage):
	"""Genomic Prediction Using SNP Codata

	Computes genomic breeding values using external information on the markers. The package fits a linear mixed model with heteroscedastic random effects, where the random effect variance is fitted using a linear predictor and a log link. The method is described in Mouresan, Selle and Ronnegard (2019) <doi:10.1101/636746>.
	"""
	
	cran = "CodataGS" 

	version("1.43", md5="0f8035379187e7cfd7a0ab2844b2174c")

	depends_on("r-matrix", type=("build", "run"))
