# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAhmbook(RPackage):
	"""Functions and Data for the Book 'Applied Hierarchical Modeling
in Ecology' Vols 1 and 2

	Provides functions to simulate data sets from hierarchical ecological models, including all the simulations described in the two volume publication 'Applied Hierarchical Modeling in Ecology: Analysis of distribution, abundance and species richness in R and BUGS' by Marc Kéry and Andy Royle: volume 1 (2016, ISBN: 978-0-12-801378-6) and volume 2 (2021, ISBN: 978-0-12-809585-0), <https://www.mbr-pwrc.usgs.gov/pubanalysis/keryroylebook/>. It also has all the utility functions and data sets needed to replicate the analyses shown in the books.
	"""
	
	homepage = "https://sites.google.com/site/appliedhierarchicalmodeling/home"
	cran = "AHMbook" 

	version("0.2.9", md5="5f9e9feccacdbb274c38569340ddb4d8")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-unmarked@0.12.2:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-spdep", type=("build", "run"))
