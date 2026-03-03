# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConformalpvalue(RPackage):
	"""Computes Conformal p-Values

	Computes marginal conformal p-values using conformal prediction in binary classification tasks. Conformal prediction is a framework that augments machine learning algorithms with a measure of uncertainty, in the form of prediction regions that attain a user-specified level of confidence. This package specifically focuses on providing conformal p-values that can be used to assess the confidence of the classification predictions. For more details, see Tyagi and Guo (2023) <https://proceedings.mlr.press/v204/tyagi23a.html>.
	"""
	
	cran = "conformalpvalue" 

	version("0.1.0", md5="cce7088a16e8ce6e72ce8e922cecef49")

	depends_on("r-e1071", type=("build", "run"))
