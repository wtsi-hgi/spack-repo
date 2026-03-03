# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMateable(RPackage):
	"""Assess Mating Potential in Space and Time

	Simulate, manage, visualize, and analyze spatially and temporally 
    explicit datasets of mating potential. Implements methods to calculate 
    synchrony, proximity, and compatibility.Synchrony calculations are based on 
    methods described in Augspurger (1983) <doi:10.2307/2387650>, 
    Kempenaers (1993) <doi:10.2307/3676415>, Ison et al. (2014) 
    <doi:10.3732/ajb.1300065>, and variations on these, as described.
	"""
	
	homepage = "https://github.com/stuartWagenius/mateable"
	cran = "mateable" 

	version("0.3.2", md5="5411f30ffffadc771228244aaaa0b75e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-sn", type=("build", "run"))
