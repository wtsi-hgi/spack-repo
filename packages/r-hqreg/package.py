# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHqreg(RPackage):
	"""Regularization Paths for Lasso or Elastic-Net Penalized Huber
Loss Regression and Quantile Regression

	Efficient algorithms for fitting regularization paths for lasso or elastic-net penalized regression models with Huber loss, quantile loss or squared loss.
	"""
	
	homepage = "http://arxiv.org/abs/1509.02957"
	cran = "hqreg" 

	version("1.4", md5="3d76d50a663c156549afde564cd9a92e")

