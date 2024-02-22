# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPartools(RPackage):
	"""Tools for the 'Parallel' Package

	Miscellaneous utilities for parallelizing large
   computations.  Alternative to MapReduce.
   File splitting and distributed operations such as sort and aggregate.
   "Software Alchemy" method for parallelizing most statistical methods,
   presented in N. Matloff, Parallel Computation for Data Science,
   Chapman and Hall, 2015.  Includes a debugging aid.
	"""
	
	homepage = "https://github.com/matloff/partools"
	cran = "partools" 

	version("1.1.6", md5="1bdc211ca433cf29727c8461c723a6d6")

	depends_on("r-regtools", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-pdist", type=("build", "run"))
