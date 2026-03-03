# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimplextree(RPackage):
	"""Provides Tools for Working with General Simplicial Complexes

	Provides an interface to a Simplex Tree data structure, which is 
  a data structure aimed at enabling efficient manipulation of simplicial complexes 
  of any dimension. The Simplex Tree data structure was originally introduced by 
  Jean-Daniel Boissonnat and Clément Maria (2014) <doi:10.1007/s00453-014-9887-3>. 
	"""
	
	homepage = "https://github.com/peekxc/simplextree"
	cran = "simplextree" 

	version("1.0.1", md5="1c19887d2d9ced8d9005879b5fd0d705")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
