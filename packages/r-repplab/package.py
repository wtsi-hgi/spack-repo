# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRepplab(RPackage):
	"""R Interface to 'EPP-Lab', a Java Program for Exploratory
Projection Pursuit

	An R Interface to 'EPP-lab' v1.0. 'EPP-lab' is a Java program for
    projection pursuit using genetic algorithms written by Alain Berro and S. Larabi
    Marie-Sainte and is included in the package. 
	"""
	
	cran = "REPPlab" 

	version("0.9.6", md5="7aa595ebc19cbfd648207e06e34968ef")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-rjava", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-ldrtools@0.2:", type=("build", "run"))
