# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR2winbugs(RPackage):
	"""Running 'WinBUGS' and 'OpenBUGS' from 'R' / 'S-PLUS'

	Invoke a 'BUGS' model in 'OpenBUGS' or 'WinBUGS', a class "bugs" for 'BUGS' 
  results and functions to work with that class.
  Function write.model() allows a 'BUGS' model file to be written.  
  The class and auxiliary functions could be used with other MCMC programs, including 'JAGS'.
	"""
	
	cran = "R2WinBUGS" 

	version("2.1-22.1", md5="fed637512e1fa184fab761080cda95f9")
	version("2.1-21", md5="4dd5fd8d8bfbb2db7847506ffe355df5")

	depends_on("r@2.13:", type=("build", "run"))
	depends_on("r-coda@0.11.0:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
