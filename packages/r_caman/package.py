# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCaman(RPackage):
	"""Finite Mixture Models and Meta-Analysis Tools - Based on C.A.MAN

	Tools for the analysis of finite semiparametric mixtures.
        These are useful when data is heterogeneous, e.g. in
        pharmacokinetics or meta-analysis. The NPMLE and VEM algorithms
        (flexible support size) and EM algorithms (fixed support size)
        are provided for univariate (Bohning et al., 1992; 
        <doi:10.2307/2532756>) and bivariate data (Schlattmann et 
        al., 2015; <doi:10.1016/j.jclinepi.2014.08.013>).
	"""
	
	cran = "CAMAN" 

	version("0.78", md5="67220e62ccdb4a4a73ed77ad1c61dc8e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
