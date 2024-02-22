# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSrm(RPackage):
	"""Structural Equation Modeling for the Social Relations Model

	
    Provides functionality for structural equation modeling for
    the social relations model (Kenny & La Voie, 1984;
    <doi:10.1016/S0065-2601(08)60144-6>; Warner, Kenny, & Soto, 1979,
    <doi:10.1037/0022-3514.37.10.1742>). Maximum likelihood
    estimation (Gill & Swartz, 2001, <doi:10.2307/3316080>;
    Nestler, 2018, <doi:10.3102/1076998617741106>) and
    least squares estimation is supported (Bond & Malloy, 2018,
    <doi:10.1016/B978-0-12-811967-9.00014-X>).
	"""
	
	homepage = "https://github.com/alexanderrobitzsch/srm"
	cran = "srm" 

	version("0.4-26", md5="04a185ec594e93e5af476d24b3835cdc")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
