# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNcvreg(RPackage):
	"""Regularization Paths for SCAD and MCP Penalized Regression
Models

	Fits regularization paths for linear regression, GLM, and Cox
  regression models using lasso or nonconvex penalties, in particular the
  minimax concave penalty (MCP) and smoothly clipped absolute deviation (SCAD)
  penalty, with options for additional L2 penalties (the "elastic net" idea).
  Utilities for carrying out cross-validation as well as post-fitting
  visualization, summarization, inference, and prediction are also provided.
  For more information, see Breheny and Huang (2011) <doi:10.1214/10-AOAS388>
  or visit the ncvreg homepage <https://pbreheny.github.io/ncvreg/>.
	"""
	
	homepage = "https://pbreheny.github.io/ncvreg/"
	cran = "ncvreg" 

	version("3.14.1", md5="cc1cd8336eb2a48cb59020dcdc459011")

