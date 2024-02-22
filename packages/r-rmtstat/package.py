# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmtstat(RPackage):
	"""Distributions, Statistics and Tests Derived from Random Matrix
Theory

	
    Functions for working with the Tracy-Widom laws and other distributions 
    related to the eigenvalues of large Wishart matrices.
    The tables for computing the Tracy-Widom densities and distribution
    functions were computed by functions were computed by Momar Dieng's MATLAB package "RMLab". This package is part of a collaboration between Iain Johnstone, Zongming Ma, Patrick Perry, and Morteza Shahram.
	"""
	
	homepage = "https://github.com/evanbiederstedt/RMTstat"
	cran = "RMTstat" 

	version("0.3.1", md5="71e2f2fd478902ab0135522b01d15e95")

