# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPreventr(RPackage):
	"""An Implementation of the AHA PREVENT Equations

	Implements the American Heart Association (AHA) Predicting
    Risk of cardiovascular disease EVENTs (PREVENT) equations from Khan
    SS, Matsushita K, Sang Y, and colleagues (2024)
    <doi:10.1161/CIRCULATIONAHA.123.067626>.
	"""
	
	homepage = "https://martingmayer.com/preventr"
	cran = "preventr" 

	version("0.9.0", md5="b9124e58d6cf2fbb5bb473e5e5a4c2f0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
