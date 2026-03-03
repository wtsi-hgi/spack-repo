# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR4dsTutorials(RPackage):
	"""Tutorials for "R for Data Science"

	When assigned "R for Data Science" (Wickham, Çetinkaya-Rundel, 
  and Grolemund (2023, ISBN: 1492097402)), students should read the book and
  type in all the associated R commands themselves. Sadly, that never happens.
  These tutorials allow students to demonstrate (and their instructors
  to be sure) that all work has been completed. See Kane (2023)
  <https://ppbds.github.io/tutorial.helpers/articles/instructions.html> from
  the 'tutorial.helpers' package for a background discussion.
	"""
	
	homepage = "https://ppbds.github.io/r4ds.tutorials/"
	cran = "r4ds.tutorials" 

	version("0.2.0", md5="e48b18a83a459646b9a8a2f62d8f994c")

	depends_on("r-tutorial-helpers", type=("build", "run"))
