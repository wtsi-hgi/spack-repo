# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGa(RPackage):
	"""Genetic Algorithms

	Flexible general-purpose toolbox implementing genetic 
  algorithms (GAs) for stochastic optimisation. Binary, real-valued, and
  permutation representations are available to optimize a fitness 
  function, i.e. a function provided by users depending on their 
  objective function. Several genetic operators are available and can be
  combined to explore the best settings for the current task. 
  Furthermore, users can define new genetic operators and easily 
  evaluate their performances. Local search using general-purpose 
  optimisation algorithms can be applied stochastically to exploit 
  interesting regions. GAs can be run sequentially or in parallel, using
  an explicit master-slave parallelisation or a coarse-grain islands 
  approach. For more details see Scrucca (2013) 
  <doi:10.18637/jss.v053.i04> and Scrucca (2017) 
  <doi:10.32614/RJ-2017-008>.
	"""
	
	homepage = "https://luca-scr.github.io/GA/"
	cran = "GA" 

	version("3.2.4", md5="af1d5666b86f2cb8a5eb18329d063115")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
