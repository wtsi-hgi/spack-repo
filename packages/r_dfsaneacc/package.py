# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDfsaneacc(RPackage):
	"""Accelerated Derivative-Free Method for Large-Scale Nonlinear
Systems of Equations

	Secant acceleration applied to derivative-free Spectral
  Residual Methods for solving large-scale nonlinear systems of
  equations. The main reference follows: E. G. Birgin and
  J. M. Martinez (2022) <doi:10.1137/20M1388024>.
	"""
	
	cran = "dfsaneacc" 

	version("1.0.2", md5="f2b828f2cfd0fe85248b1b511d5b803c")

