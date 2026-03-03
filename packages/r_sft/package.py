# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSft(RPackage):
	"""Functions for Systems Factorial Technology Analysis of Data

	A series of tools for analyzing Systems Factorial Technology data.  This includes functions for plotting and statistically testing capacity coefficient functions and survivor interaction contrast functions.  Houpt, Blaha, McIntire, Havig, and Townsend (2013) <doi:10.3758/s13428-013-0377-3> provide a basic introduction to Systems Factorial Technology along with examples using the sft R package.
	"""
	
	cran = "sft" 

	version("2.2-1", md5="244c66184e02c9a549d5ed1b6a012fc1")

	depends_on("r@1.8:", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-suppdists", type=("build", "run"))
