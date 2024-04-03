# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmumps(RPackage):
	"""Wrapper for MUMPS Library

	Some basic features of 'MUMPS' (Multifrontal Massively Parallel
         sparse direct Solver) are wrapped in a class whose methods can be used
         for sequentially solving a sparse linear system (symmetric or not)
         with one or many right hand sides (dense or sparse).
         There is a possibility to do separately symbolic analysis,
         LU (or LDL^t) factorization and system solving.
         Third part ordering libraries are included and can be used: 'PORD', 'METIS', 'SCOTCH'.
         'MUMPS' method was first described in Amestoy et al. (2001) <doi:10.1137/S0895479899358194>
         and Amestoy et al. (2006) <doi:10.1016/j.parco.2005.07.004>.
	"""
	
	homepage = "http://www.mumps-solver.org/"
	cran = "rmumps" 

	version("5.2.1-29", md5="5cff3e513fddd201004c88976eb11d47")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))
