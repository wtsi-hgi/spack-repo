# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRxode2(RPackage):
	"""Facilities for Simulating from ODE-Based Models

	Facilities for running simulations from ordinary
    differential equation ('ODE') models, such as pharmacometrics and other
    compartmental models.  A compilation manager translates the ODE model
    into C, compiles it, and dynamically loads the object code into R for
    improved computational efficiency.  An event table object facilitates
    the specification of complex dosing regimens (optional) and sampling
    schedules.  NB: The use of this package requires both C and
    Fortran compilers, for details on their use with R please see
    Section 6.3, Appendix A, and Appendix D in the "R Administration and
    Installation" manual. Also the code is mostly released under GPL.  The
    'VODE' and 'LSODA' are in the public domain.  The information is available
    in the inst/COPYRIGHTS.
	"""
	
	homepage = "https://nlmixr2.github.io/rxode2/"
	cran = "rxode2" 

	version("2.1.2", md5="ebe4d746ae0f3a3b84bd6e8cd02f6fcf", url="https://cran.r-project.org/src/contrib/rxode2_2.1.2.tar.gz")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-precisesums@0.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-backports", type=("build", "run"))
	depends_on("r-cli@2:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-inline", type=("build", "run"))
	depends_on("r-lotri@0.4:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-rex", type=("build", "run"))
	depends_on("r-sys", type=("build", "run"))
	depends_on("r-rxode2ll@2.0.9:", type=("build", "run"))
	depends_on("r-rxode2et@2.0.9:", type=("build", "run"))
	depends_on("r-rxode2parse@2.0.12:", type=("build", "run"))
	depends_on("r-rxode2random", type=("build", "run"))
	depends_on("r-data-table@1.12.4:", type=("build", "run"))
	depends_on("r-qs", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.9.300.2:", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
