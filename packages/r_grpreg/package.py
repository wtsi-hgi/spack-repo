# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrpreg(RPackage):
	"""Regularization Paths for Regression Models with Grouped
Covariates

	Efficient algorithms for fitting the regularization path of linear
  regression, GLM, and Cox regression models with grouped penalties.  This
  includes group selection methods such as group lasso, group MCP, and
  group SCAD as well as bi-level selection methods such as the group
  exponential lasso, the composite MCP, and the group bridge.  For more
  information, see Breheny and Huang (2009) <doi:10.4310/sii.2009.v2.n3.a10>,
  Huang, Breheny, and Ma (2012) <doi:10.1214/12-sts392>, Breheny and Huang
  (2015) <doi:10.1007/s11222-013-9424-2>, and Breheny (2015)
  <doi:10.1111/biom.12300>, or visit the package homepage
  <https://pbreheny.github.io/grpreg/>.
	"""
	
	homepage = "https://pbreheny.github.io/grpreg/"
	cran = "grpreg" 

	version("3.4.0", md5="bc7e8148a92adc041f15a05bf243e700")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
