# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCste(RPackage):
	"""Covariate Specific Treatment Effect (CSTE) Curve

	A uniform  statistical inferential tool in making individualized treatment decisions, which implements the methods of Ma et al. (2017)<DOI:10.1177/0962280214541724> 
    and Guo et al. (2021)<DOI:10.1080/01621459.2020.1865167>. It uses a flexible semiparametric modeling strategy for heterogeneous treatment effect estimation in high-dimensional settings and can gave valid confidence bands. Based on it, one can find the subgroups of patients that benefit from each treatment, thereby making individualized treatment selection.
	"""
	
	cran = "CSTE" 

	version("2.0.0", md5="c915d448f79d5275449a4c8d69f92e5a")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-locpol", type=("build", "run"))
	depends_on("r-dfoptim", type=("build", "run"))
