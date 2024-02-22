# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROccumb(RPackage):
	"""Site Occupancy Modeling for Environmental DNA Metabarcoding

	Fits multispecies site occupancy models to environmental DNA
    metabarcoding data collected using spatially-replicated survey design.
    Model fitting results can be used to evaluate and compare the effectiveness
    of species detection to find an efficient survey design.
    Reference: Fukaya et al. (2022) <doi:10.1111/2041-210X.13732>.
	"""
	
	homepage = "https://fukayak.github.io/occumb/"
	cran = "occumb" 

	version("1.0.3", md5="3ace98b2ccec1963971b9c1ba8396054")

	depends_on("r-jagsui", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("jags", type=("build", "link", "run"))
