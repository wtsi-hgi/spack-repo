# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimmer(RPackage):
	"""Discrete-Event Simulation for R

	A process-oriented and trajectory-based Discrete-Event Simulation
    (DES) package for R. It is designed as a generic yet powerful framework. The
    architecture encloses a robust and fast simulation core written in 'C++' with
    automatic monitoring capabilities. It provides a rich and flexible R API that
    revolves around the concept of trajectory, a common path in the simulation
    model for entities of the same type. Documentation about 'simmer' is provided
    by several vignettes included in this package, via the paper by Ucar, Smeets
    & Azcorra (2019, <doi:10.18637/jss.v090.i02>), and the paper by Ucar,
    Hernández, Serrano & Azcorra (2018, <doi:10.1109/MCOM.2018.1700960>);
    see 'citation("simmer")' for details.
	"""
	
	homepage = "https://r-simmer.org"
	cran = "simmer" 

	version("4.4.6.3", md5="bf9c93a8dacef8dd78002044d86a15af")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp@0.12.9:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-codetools", type=("build", "run"))
