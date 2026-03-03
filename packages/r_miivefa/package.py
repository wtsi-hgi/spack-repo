# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMiivefa(RPackage):
	"""Exploratory Factor Analysis Using Model Implied Instrumental
Variables

	Data-driven approach for Exploratory Factor Analysis (EFA)
    that uses Model Implied Instrumental Variables (MIIVs). The method
    starts with a one factor model and arrives at a suggested model with
    enhanced interpretability that allows cross-loadings and correlated
    errors.
	"""
	
	homepage = "https://github.com/lluo0/MIIVefa/"
	cran = "MIIVefa" 

	version("0.1.2", md5="a1dcdaba0c4b9ddb7e3ccaf94507679b")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-miivsem", type=("build", "run"))
