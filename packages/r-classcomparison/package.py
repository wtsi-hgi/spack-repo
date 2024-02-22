# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClasscomparison(RPackage):
	"""Classes and Methods for "Class Comparison" Problems on
Microarrays

	Defines the classes used for "class comparison" problems
  in the OOMPA project (<http://oompa.r-forge.r-project.org/>). Class
  comparison includes tests for differential expression; see Simon's
  book for details on typical problem types.
	"""
	
	homepage = "http://oompa.r-forge.r-project.org/"
	cran = "ClassComparison" 

	version("3.1.8", md5="84cd09999b50e462e62deea0abe5977b")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-oompabase@3:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
