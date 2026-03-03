# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRedm(RPackage):
	"""Empirical Dynamic Modeling ('EDM')

	An implementation of 'EDM' algorithms based on research software developed for internal use at the Sugihara Lab ('UCSD/SIO').  The package is implemented with 'Rcpp' wrappers around the 'cppEDM' library.  It implements the 'simplex' projection method from Sugihara & May (1990) <doi:10.1038/344734a0>, the 'S-map' algorithm from Sugihara (1994) <doi:10.1098/rsta.1994.0106>, convergent cross mapping described in Sugihara et al. (2012) <doi:10.1126/science.1227079>, and, 'multiview embedding' described in Ye & Sugihara (2016) <doi:10.1126/science.aag0863>.
	"""
	
	cran = "rEDM" 

	version("1.15.3", md5="a5c13071ea562786fae33502fdd33378")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppthread", type=("build", "run"))
