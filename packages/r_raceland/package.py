# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRaceland(RPackage):
	"""Pattern-Based Zoneless Method for Analysis and Visualization of
Racial Topography

	Implements a computational framework for a pattern-based, 
    zoneless analysis, and visualization of (ethno)racial topography 
    (Dmowska, Stepinski, and Nowosad (2020) <doi:10.1016/j.apgeog.2020.102239>).
    It is a reimagined
    approach for analyzing residential segregation and racial diversity based on 
    the concept of 'landscape’ used in the domain of landscape ecology.
	"""
	
	homepage = "https://jakubnowosad.com/raceland/"
	cran = "raceland" 

	version("1.2.1", md5="ea8ee26e8f67ca454df6a486254cc9b3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-plotwidgets", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-comat@0.9:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
