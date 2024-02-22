# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRandomforest(RPackage):
	"""Breiman and Cutler's Random Forests for Classification and Regression.

	Classification and regression based on a forest of trees using random
	inputs."""

	cran = "randomForest"

	version("4.7-1.1", md5="605493f557b7ba08151062e7d1a63495")

	depends_on("r@4.1:", type=("build", "run"))
