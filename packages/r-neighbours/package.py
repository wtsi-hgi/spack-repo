# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNeighbours(RPackage):
	"""Neighbourhood Functions for Local-Search Algorithms

	Neighbourhood functions are key components of
  local-search algorithms such as Simulated Annealing or
  Threshold Accepting.  These functions take a solution and
  return a slightly-modified copy of it, i.e. a neighbour.
  The package provides a function neighbourfun() that
  constructs such neighbourhood functions, based on
  parameters such as admissible ranges for elements in a
  solution.  Supported are numeric and logical solutions.
  The algorithms were originally created for
  portfolio-optimisation applications, but can be used for
  other models as well.  Several recipes for neighbour
  computations are taken from "Numerical Methods and
  Optimization in Finance" by M. Gilli, D. Maringer and
  E. Schumann (2019, ISBN:978-0128150658).
	"""
	
	homepage = "http://enricoschumann.net/R/packages/neighbours/"
	cran = "neighbours" 

	version("0.1-3", md5="9e7bb3ea676eb648e30f7eaeb13e5381")

	depends_on("r@3.3:", type=("build", "run"))
