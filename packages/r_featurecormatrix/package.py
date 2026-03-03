# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFeaturecormatrix(RPackage):
	"""Measurement Level Independent Feature Correlation Matrix

	Uses three different correlation coefficients to
    calculate measurement-level adequate correlations in a feature matrix: 
    Pearson product-moment correlation coefficient,
    Intraclass correlation and Cramer's V.
	"""
	
	cran = "featureCorMatrix" 

	version("0.4.0", md5="33c06248a9af71d5cb8f93c783ce2882")

