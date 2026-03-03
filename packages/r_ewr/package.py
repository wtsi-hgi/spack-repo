# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REwr(RPackage):
	"""Econometrics with R

	Function and data sets in the book entitled "R ile Temel Ekonometri", S.Guris, E.C.Akay, B. Guris(2020). The book published in Turkish. It is possible to makes Durbin two stage method for autocorrelation, generalized differencing method for correction autocorrelation, Hausman Test for identification and computes LM, LR and Wald test statistics for redundant variable by using the functions written in this package. 
	"""
	
	cran = "EwR" 

	version("1.4", md5="2816b21f9d621c9404acd43b510ae52e")

	depends_on("r@3.5:", type=("build", "run"))
