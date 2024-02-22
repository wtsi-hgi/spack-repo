# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobumeta(RPackage):
	"""Robust Variance Meta-Regression

	Functions for conducting robust variance estimation (RVE) meta-regression using both large and small sample RVE estimators under various weighting schemes. These methods are distribution free and provide valid point estimates, standard errors and hypothesis tests even when the degree and structure of dependence between effect sizes is unknown. Also included are functions for conducting sensitivity analyses under correlated effects weighting and producing RVE-based forest plots. 
	"""
	
	homepage = "https://github.com/zackfisher/robumeta"
	cran = "robumeta" 

	version("2.1", md5="8f80a79fc262c49172df2bcf78e3e1e3")

