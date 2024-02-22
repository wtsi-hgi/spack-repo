# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlindleyroc(RPackage):
	"""Receiver Operating Characteristic Based on Power Lindley
Distribution

	Receiver Operating Characteristic (ROC) analysis is performed assuming samples are from the Power Lindley distribution. Specificity, sensitivity, area under the curve and ROC curve are provided.
	"""
	
	homepage = "https://github.com/ErtanSU/PLindleyROC"
	cran = "PLindleyROC" 

	version("0.1.1", md5="0d166ea0fdcc8f3b6da5e92892ed2499")

