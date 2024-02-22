# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSampleselection(RPackage):
	"""Sample Selection Models

	Two-step
   and maximum likelihood estimation
   of Heckman-type sample selection models:
   standard sample selection models (Tobit-2),
   endogenous switching regression models (Tobit-5),
   sample selection models with binary dependent outcome variable,
   interval regression with sample selection (only ML estimation),
   and endogenous treatment effects models.
   These methods are described in the three vignettes
   that are included in this package 
   and in econometric textbooks such as
   Greene (2011, Econometric Analysis, 7th edition, Pearson).
	"""
	
	homepage = "http://www.sampleSelection.org"
	cran = "sampleSelection" 

	version("1.2-12", md5="f64dba3ee084522778f3fe7f33c60ba4")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-maxlik@0.7.3:", type=("build", "run"))
	depends_on("r-misctools@0.6.3:", type=("build", "run"))
	depends_on("r-systemfit@1.0.0:", type=("build", "run"))
	depends_on("r-formula@1.1.1:", type=("build", "run"))
	depends_on("r-vgam@1.1.1:", type=("build", "run"))
	depends_on("r-mvtnorm@0.9.9994:", type=("build", "run"))
