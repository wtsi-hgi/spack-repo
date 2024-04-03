# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RO2geosocial(RPackage):
	"""Reconstruction of Transmission Chains from Surveillance Data

	Bayesian reconstruction of who infected whom during past outbreaks using routinely-collected surveillance data. Inference of transmission trees using genotype, age specific social contacts, distance between cases and onset dates of the reported cases. (Robert A, Kucharski AJ, Gastanaduy PA, Paul P, Funk S. (2020) <doi:10.1098/rsif.2020.0084>).
	"""
	
	homepage = "https://github.com/alxsrobert/o2geosocial"
	cran = "o2geosocial" 

	version("1.1.2", md5="199e6156d7fe2ef6bc8d1e6d298f49f9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-outbreaker2", type=("build", "run"))
