# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWeightedroc(RPackage):
	"""Fast, Weighted ROC Curves

	Fast computation of
 Receiver Operating Characteristic (ROC) curves
 and Area Under the Curve (AUC)
 for weighted binary classification problems
 (weights are example-specific cost values).
	"""
	
	homepage = "https://github.com/tdhock/WeightedROC"
	cran = "WeightedROC" 

	version("2020.1.31", md5="3aea73ddc286499e26b3ed5f8336bd9c")

