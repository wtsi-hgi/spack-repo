# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAst(RPackage):
	"""Age-Spatial-Temporal Model

	Fits a model to adjust and consider additional variations in three dimensions of age groups, time, and space on residuals excluded from a prediction model that have residual such as: linear regression, mixed model and so on. Details are given in Foreman et al. (2015) <doi:10.1186/1478-7954-10-1>.
	"""
	
	cran = "AST" 

	version("0.1.0", md5="1394552f781d8125101549a448c7d2f1")

	depends_on("r@3:", type=("build", "run"))
