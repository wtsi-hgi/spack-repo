# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExactmed(RPackage):
	"""Exact Mediation Analysis for Binary Outcomes

	A tool for conducting exact parametric regression-based causal mediation analysis of binary outcomes 
    as described in Samoilenko, Blais and Lefebvre (2018) <doi:10.1353/obs.2018.0013>;
    Samoilenko, Lefebvre (2021) <doi:10.1093/aje/kwab055>; and Samoilenko, Lefebvre (2023) <doi:10.1002/sim.9621>.
	"""
	
	homepage = "https://caubm.github.io/ExactMed/"
	cran = "ExactMed" 

	version("0.3.0", md5="0469c9417c9b1cbee3abb99d84033f95")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-brglm2", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-pkgcond", type=("build", "run"))
	depends_on("r-mlogit", type=("build", "run"))
	depends_on("r-dfidx", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
