# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDegross(RPackage):
	"""Density Estimation from GROuped Summary Statistics

	Estimation of a density from grouped (tabulated) summary statistics evaluated in each of the big bins (or classes) partitioning the support of the variable. These statistics include class frequencies and central moments of order one up to four. The log-density is modelled using a linear combination of penalised B-splines. The multinomial log-likelihood involving the frequencies adds up to a roughness penalty based on the differences in the coefficients of neighbouring B-splines and the log of a root-n approximation of the sampling density of the observed vector of central moments in each class. The so-obtained penalized log-likelihood is maximized using the EM algorithm to get an estimate of the spline parameters and, consequently, of the variable density and related quantities such as quantiles, see Lambert, P. (2021) <arXiv:2107.03883> for details.
	"""
	
	cran = "degross" 

	version("0.9.0", md5="84e8ff8da91b54286f89df2b9a8c65fa")

	depends_on("r-cubicbsplines", type=("build", "run"))
