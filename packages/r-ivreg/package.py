# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIvreg(RPackage):
	"""Instrumental-Variables Regression by '2SLS', '2SM', or '2SMM',
with Diagnostics

	Instrumental variable estimation for linear models by two-stage least-squares (2SLS) regression or by robust-regression via M-estimation (2SM) or MM-estimation (2SMM). The main ivreg() model-fitting function is designed to provide a workflow as similar as possible to standard lm() regression. A wide range of methods is provided for fitted ivreg model objects, including extensive functionality for computing and graphing regression diagnostics in addition to other standard model tools.
	"""
	
	homepage = "https://zeileis.github.io/ivreg/"
	cran = "ivreg" 

	version("0.6-2", md5="9221729c0eb7b31dd7dd6bc8f373931d")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-car@3.0.9:", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
