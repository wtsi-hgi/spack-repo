# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHagis(RPackage):
	"""Analysis of Plant Pathogen Pathotype Complexities, Distributions
and Diversity

	Analysis of plant pathogen pathotype survey data.  Functions
  provided calculate distribution of susceptibilities, distribution of
  complexities with statistics, pathotype frequency distribution, as well as
  diversity indices for pathotypes.  This package is meant to be a direct
  replacement for Herrmann, Löwer and Schachtel's (1999)
  <doi:10.1046/j.1365-3059.1999.00325.x> Habgood-Gilmour Spreadsheet, 'HaGiS',
  previously used for pathotype analysis.
	"""
	
	homepage = "https://github.com/openplantpathology/hagis"
	cran = "hagis" 

	version("3.1.11", md5="48eac644d81f28916ca8db349a01a808")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-pander", type=("build", "run"))
