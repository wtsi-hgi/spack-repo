# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiffeqr(RPackage):
	"""Solving Differential Equations (ODEs, SDEs, DDEs, DAEs)

	An interface to 'DifferentialEquations.jl' <https://diffeq.sciml.ai/dev/> from the R programming language.
  It has unique high performance methods for solving ordinary differential equations (ODE), stochastic differential equations (SDE),
  delay differential equations (DDE), differential-algebraic equations (DAE), and more. Much of the functionality,
  including features like adaptive time stepping in SDEs, are unique and allow for multiple orders of magnitude speedup over more common methods.
  Supports GPUs, with support for CUDA (NVIDIA), AMD GPUs, Intel oneAPI GPUs, and Apple's Metal (M-series chip GPUs).
  'diffeqr' attaches an R interface onto the package, allowing seamless use of this tooling by R users. For more information,
  see Rackauckas and Nie (2017) <doi:10.5334/jors.151>.
	"""
	
	homepage = "https://github.com/SciML/diffeqr"
	cran = "diffeqr" 

	version("2.0.0", md5="c811e49721444a253582e616d7187e62")
	version("2.0.1", md5="56eb543f263f21d056df2ecae2803bf3")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-juliacall", type=("build", "run"))
	depends_on("julia@1.6:", type=("build", "link", "run"))
