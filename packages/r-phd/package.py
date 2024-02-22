# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhd(RPackage):
	"""Permutation Testing in High-Dimensional Linear Models

	Provides permutation methods for testing in high-dimensional linear models.
    The tests are often robust against heteroscedasticity and non-normality 
    and usually perform well under anti-sparsity.
    See Hemerik, Thoresen and Finos (2021) <doi:10.1080/00949655.2020.1836183>.
	"""
	
	cran = "phd" 

	version("0.2", md5="eb219c3137e82f8a7ed541e2e50a4473")

	depends_on("r-glmnet", type=("build", "run"))
