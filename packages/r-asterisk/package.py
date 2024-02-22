# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAsterisk(RPackage):
	"""Computation of Satellite Position

	Provides basic functionalities to calculate the position of
    satellites given a known state vector. The package includes implementations
    of the SGP4 and SDP4 simplified perturbation models to propagate orbital
    state vectors, as well as utilities to read TLE files and convert coordinates
    between different frames of reference. Several of the functionalities of the
    package (including the high-precision numerical orbit propagator) require
    the coefficients and data included in the 'asteRiskData' package, available
    in a 'drat' repository. To install this data package, run 
    'install.packages("asteRiskData", repos="https://rafael-ayala.github.io/drat/")'.
    Felix R. Hoots, Ronald L. Roehrich and T.S. Kelso (1988) <https://celestrak.org/NORAD/documentation/spacetrk.pdf>.
    David Vallado, Paul Crawford, Richard Hujsak and T.S. Kelso (2012) <doi:10.2514/6.2006-6753>.
    Felix R. Hoots, Paul W. Schumacher Jr. and Robert A. Glover (2014) <doi:10.2514/1.9161>.
	"""
	
	cran = "asteRisk" 

	version("1.4.3", md5="444b834a08a59289708722952047b4b3")

	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-nanotime", type=("build", "run"))
	depends_on("r-onion", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
