# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrivatelr(RPackage):
	"""Differentially Private Regularized Logistic Regression

	Implements two differentially private algorithms for 
  estimating L2-regularized logistic regression coefficients. A randomized
  algorithm F is epsilon-differentially private (C. Dwork, Differential
  Privacy, ICALP 2006 <DOI:10.1007/11681878_14>), if 
     |log(P(F(D) in S)) - log(P(F(D') in S))| <= epsilon
  for any pair D, D' of datasets that differ in exactly one record, any
  measurable set S, and the randomness is taken over the choices F makes. 
	"""
	
	cran = "PrivateLR" 

	version("1.2-22", md5="638f1a8c266bedee42ddfb31423d3bbe")

