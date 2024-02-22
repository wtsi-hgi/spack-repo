# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRct2(RPackage):
	"""Designing and Analyzing Two-Stage Randomized Experiments

	Provides various statistical methods for designing and analyzing two-stage randomized controlled 
	trials using the methods developed by Imai, Jiang, and Malani (2021) <doi:10.1080/01621459.2020.1775612> and 
	(2022+) <doi:10.48550/arXiv.2011.07677>.  The package enables the estimation of direct and spillover effects, 
	conduct hypotheses tests, and conduct sample size calculation for two-stage randomized controlled trials.  
	"""
	
	homepage = "https://github.com/kosukeimai/RCT2"
	cran = "RCT2" 

	version("0.0.1", md5="5bf6af81fb6578bc222c3164627071a2", url="https://cran.r-project.org/src/contrib/RCT2_0.0.1.tar.gz")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-aer", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
