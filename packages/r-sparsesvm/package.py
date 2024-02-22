# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparsesvm(RPackage):
	"""Solution Paths of Sparse High-Dimensional Support Vector Machine
with Lasso or Elastic-Net Regularization

	Fast algorithm for fitting solution paths of sparse SVM models with lasso or elastic-net regularization.
	"""
	
	cran = "sparseSVM" 

	version("1.1-6", md5="4f793ba9ad7414bdf071f5d244c2654c")

