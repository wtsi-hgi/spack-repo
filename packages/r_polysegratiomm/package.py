# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPolysegratiomm(RPackage):
	"""Bayesian Mixture Models for Marker Dosage in Autopolyploids

	Fits Bayesian mixture models to estimate marker dosage for dominant markers in autopolyploids using JAGS (1.0 or greater) as outlined in Baker et al "Bayesian estimation of marker dosage in sugarcane and other autopolyploids" (2010, <doi:10.1007/s00122-010-1283-z>). May be used in conjunction with polySegratio for simulation studies and comparison with standard methods.
	"""
	
	homepage = "https://github.com/petebaker/polysegratiomm"
	cran = "polySegratioMM" 

	version("0.6-4", md5="8d06773cfd9ce2e8bf73a5c786d366cb")

	depends_on("r@2.12:", type=("build", "run"))
	depends_on("r-polysegratio", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
