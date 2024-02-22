# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNsga2r(RPackage):
	"""Elitist Non-Dominated Sorting Genetic Algorithm

	Box-constrained multiobjective optimization using the 
        elitist non-dominated sorting genetic algorithm - NSGA-II.
        Fast non-dominated sorting, crowding distance, tournament 
        selection, simulated binary crossover, and polynomial 
        mutation are called in the main program. The methods are 
        described in Deb et al. (2002) <doi:10.1109/4235.996017>.
	"""
	
	cran = "nsga2R" 

	version("1.1", md5="d651c789c8a43bf6ae619ee16756dc94")

	depends_on("r-mco", type=("build", "run"))
