# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQap(RPackage):
	"""Heuristics for the Quadratic Assignment Problem (QAP)

	Implements heuristics for the Quadratic Assignment Problem (QAP). Although, the QAP was introduced as a combinatorial optimization problem for the facility location problem in operations research, it also has many applications in data analysis. The problem is NP-hard and the package implements a simulated annealing heuristic.
	"""
	
	homepage = "https://github.com/mhahsler/qap"
	cran = "qap" 

	version("0.1-2", md5="b809a006c224259c932942f0dccb3577")

