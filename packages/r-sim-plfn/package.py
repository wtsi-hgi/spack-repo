# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimPlfn(RPackage):
	"""Simulation of Piecewise Linear Fuzzy Numbers

	The definition of fuzzy random variable and the methods of simulation from fuzzy random variables are two challenging statistical problems in three recent decades. This package is organized based on a special definition of fuzzy random variable and simulate fuzzy random variable by Piecewise Linear Fuzzy Numbers (PLFNs); see Coroianua et al. (2013) <doi:10.1016/j.fss.2013.02.005> for details about PLFNs. Some important statistical functions are considered for obtaining the membership function of main statistics, such as mean, variance, summation, standard deviation and coefficient of variance. Some of applied advantages of 'Sim.PLFN' package are:  (1) Easily generating / simulation a random sample of PLFN, (2) drawing the membership functions of the simulated PLFNs or the membership function of the statistical result, and (3) Considering the simulated PLFNs for arithmetic operation or importing into some statistical computation. Finally, it must be mentioned that 'Sim.PLFN' package works on the basis of 'FuzzyNumbers' package. 
	"""
	
	cran = "Sim.PLFN" 

	version("1.0", md5="e1433e98b89be02e24c21246258c59d7")

	depends_on("r-fuzzynumbers", type=("build", "run"))
	depends_on("r-distrib", type=("build", "run"))
