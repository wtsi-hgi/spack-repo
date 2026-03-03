# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptimbase(RPackage):
	"""R Port of the 'Scilab' Optimbase Module

	Provides a set of commands to manage an abstract
        optimization method. The goal is to provide a building block
        for a large class of specialized optimization methods. This
        package manages: the number of variables, the minimum and
        maximum bounds, the number of non linear inequality
        constraints, the cost function, the logging system, various
        termination criteria, etc...
	"""
	
	cran = "optimbase" 

	version("1.0-10", md5="debfc9a4255a391bf4a61b087d7d7552")

	depends_on("r-matrix", type=("build", "run"))
