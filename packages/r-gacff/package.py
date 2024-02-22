# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGacff(RPackage):
	"""Genetic Similarity in User-Based Collaborative Filtering

	The genetic algorithm can be used directly to find the similarity of users and more effectively to increase the efficiency of the collaborative filtering method.
  By identifying the nearest neighbors to the active user, before the genetic algorithm, and by identifying suitable starting points, an effective method for user-based collaborative filtering method has been developed.
  This package uses an optimization algorithm (continuous genetic algorithm) to directly find the optimal similarities between active users (users for whom current recommendations are made) and others.
  First, by determining the nearest neighbor and their number, the number of genes in a chromosome is determined. Each gene represents the neighbor's similarity to the active user.
  By estimating the starting points of the genetic algorithm, it quickly converges to the optimal solutions.
  The positive point is the independence of the genetic algorithm on the number of data that for big data is an effective help in solving the problem.
	"""
	
	cran = "GACFF" 

	version("1.0", md5="7ce4999e76f8303c4d44b17ffe20421e")

	depends_on("r@3:", type=("build", "run"))
