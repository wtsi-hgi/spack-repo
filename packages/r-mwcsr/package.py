# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMwcsr(RPackage):
	"""Solvers for Maximum Weight Connected Subgraph Problem and Its
Variants

	Algorithms for solving various Maximum
    Weight Connected Subgraph Problems, including variants with
    budget constraints, cardinality constraints, weighted edges and signals.
    The package represents an R interface to high-efficient solvers based on
    relax-and-cut approach (Álvarez-Miranda E., Sinnl M. (2017) <doi:10.1016/j.cor.2017.05.015>)
    mixed-integer programming (Loboda A., Artyomov M., and Sergushichev A. (2016) <doi:10.1007/978-3-319-43681-4_17>)
    and simulated annealing.
	"""
	
	homepage = "https://github.com/ctlab/mwcsr"
	cran = "mwcsr" 

	version("0.1.8", md5="1081f613fa98efb7e48eeee25c55240e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("openjdk@1.8:", type=("build", "link", "run"))
