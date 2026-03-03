# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsu(RPackage):
	"""Multivariate Symmetric Uncertainty and Other Measurements

	Estimators for multivariate symmetrical uncertainty based
    on the work of Gustavo Sosa et al. (2016) <arXiv:1709.08730>,
    total correlation, information gain and symmetrical uncertainty of
    categorical variables.
	"""
	
	cran = "msu" 

	version("0.0.1", md5="d42e15d352201f885540ca1a6030ec4e")

	depends_on("r@3.4.1:", type=("build", "run"))
	depends_on("r-entropy@1.2.1:", type=("build", "run"))
