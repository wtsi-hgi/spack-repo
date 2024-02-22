# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKnnvs(RPackage):
	"""k Nearest Neighbors with Grid Search Variable Selection

	k Nearest Neighbors with variable selection, combine grid search and forward selection to achieve variable selection in order to improve k Nearest Neighbors predictive performance.
	"""
	
	cran = "kNNvs" 

	version("0.1.0", md5="34c23897ef696cbc3dc7a40d7cfc0af9")

