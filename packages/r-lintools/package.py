# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLintools(RPackage):
	"""Manipulation of Linear Systems of (in)Equalities

	Variable elimination (Gaussian elimination, Fourier-Motzkin elimination), 
    Moore-Penrose pseudoinverse, reduction to reduced row echelon form, value substitution,  
    projecting a vector on the convex polytope described by a system of (in)equations, 
    simplify systems by removing spurious columns and rows and collapse implied equalities, 
    test if a matrix is totally unimodular, compute variable ranges implied by linear
    (in)equalities.
	"""
	
	homepage = "https://github.com/data-cleaning/lintools"
	cran = "lintools" 

	version("0.1.7", md5="28e9c9ea20e3f5a1ae70b7b434d928dc")

