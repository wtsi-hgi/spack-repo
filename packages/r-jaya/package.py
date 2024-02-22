# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJaya(RPackage):
	"""Jaya, a Gradient-Free Optimization Algorithm

	Maximization or Minimization of a fitness function using Jaya Algorithm (JA).
   A population based method which repeatedly modifies a population of individual solutions.
   Capable of solving both constrained and unconstrained optimization problems.
   It does not contain any hyperparameters. 
   For further details: R.V. Rao (2016) <doi:10.5267/j.ijiec.2015.8.004> .
	"""
	
	cran = "Jaya" 

	version("0.1.9", md5="68826d4df3aa9230fbeeaebe153f6d60")

	depends_on("r-ga", type=("build", "run"))
