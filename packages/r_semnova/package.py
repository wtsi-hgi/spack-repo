# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSemnova(RPackage):
	"""Latent Repeated Measures ANOVA

	Latent repeated measures ANOVA (L-RM-ANOVA) is a structural 
    equation modeling based alternative to traditional repeated measures ANOVA.
    L-RM-ANOVA extends the latent growth components approach by 
    Mayer et al. (2012) <doi:10.1080/10705511.2012.713242> and introduces
    latent variables to repeated measures analysis.
	"""
	
	cran = "semnova" 

	version("0.1-6", md5="922f75fd4c672c71a2aaf4f49002ff2b")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
