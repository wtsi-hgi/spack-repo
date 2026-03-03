# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJlmerclusterperm(RPackage):
	"""Cluster-Based Permutation Analysis for Densely Sampled Time Data

	An implementation of fast cluster-based permutation analysis
    (CPA) for densely-sampled time data developed in Maris & Oostenveld,
    2007 <doi:10.1016/j.jneumeth.2007.03.024>. Supports (generalized,
    mixed-effects) regression models for the calculation of timewise
    statistics. Provides both a wholesale and a piecemeal interface to the
    CPA procedure with an emphasis on interpretability and diagnostics.
    Integrates 'Julia' libraries 'MixedModels.jl' and 'GLM.jl' for
    performance improvements, with additional functionalities for
    interfacing with 'Julia' from 'R' powered by the 'JuliaConnectoR'
    package.
	"""
	
	homepage = "https://github.com/yjunechoe/jlmerclusterperm"
	cran = "jlmerclusterperm" 

	version("1.1.3", md5="198c8d9241b80b2b321c7d75bb614f97")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-backports@1.1.7:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-juliaconnector", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("julia@1.8:", type=("build", "link", "run"))
