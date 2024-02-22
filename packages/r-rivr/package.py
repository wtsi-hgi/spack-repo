# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRivr(RPackage):
	"""Steady and Unsteady Open-Channel Flow Computation

	A tool for undergraduate and graduate courses in open-channel
    hydraulics. Provides functions for computing normal and critical depths,
    steady-state water surface profiles (e.g. backwater curves) and unsteady flow
    computations (e.g. flood wave routing) as described in
    Koohafkan MC, Younis BA (2015). "Open-channel computation with R."
    The R Journal, 7(2), 249–262. <doi: 10.32614/RJ-2015-034>.
	"""
	
	homepage = "https://github.com/mkoohafkan/rivr"
	cran = "rivr" 

	version("1.2-3", md5="a5437291e8abc769d81a7e0c73089f18")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
