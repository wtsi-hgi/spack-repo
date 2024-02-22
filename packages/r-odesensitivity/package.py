# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROdesensitivity(RPackage):
	"""Sensitivity Analysis of Ordinary Differential Equations

	Performs sensitivity analysis in ordinary differential equation (ode) models.
    The package utilize the ode interface from 'deSolve' and connects it with the 
    sensitivity analysis from 'sensitivity'. Additionally we add a method to
    run the sensitivity analysis on variables with class 'ODEnetwork'. A detailed
    plotting function provides outputs on the calculations.
    The method is described by Weber, Theers, Surmann, Ligges, and Weihs (2018) <doi:10.17877/DE290R-18874>.
	"""
	
	homepage = "https://github.com/surmann/ODEsensitivity"
	cran = "ODEsensitivity" 

	version("1.1.2", md5="3923a91d3db39df9e5a6f209c9437d19")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-odenetwork@1.3:", type=("build", "run"))
	depends_on("r-sensitivity@1.12.1:", type=("build", "run"))
