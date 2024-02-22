# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMize(RPackage):
	"""Unconstrained Numerical Optimization Algorithms

	Optimization algorithms implemented in R, including
    conjugate gradient (CG), Broyden-Fletcher-Goldfarb-Shanno (BFGS) and the
    limited memory BFGS (L-BFGS) methods. Most internal parameters can be set 
    through the call interface. The solvers hold up quite well for 
    higher-dimensional problems.
	"""
	
	homepage = "https://github.com/jlmelville/mize"
	cran = "mize" 

	version("0.2.4", md5="12d0e79fc61f6f4a751092f84df0e055")

