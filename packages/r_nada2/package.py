# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNada2(RPackage):
	"""Data Analysis for Censored Environmental Data

	Contains methods described by Dennis Helsel in 
             his book "Statistics for Censored Environmental Data
             using Minitab and R" (2011) and courses and videos at 
             <https://practicalstats.com>. This package adds new functions to 
             the `NADA` Package.
	"""
	
	homepage = "https://github.com/SwampThingPaul/NADA2"
	cran = "NADA2" 

	version("1.1.6", md5="b2478397e9c47b045e3ae00bd85e78a7", url="https://cran.r-project.org/src/contrib/NADA2_1.1.6.tar.gz")
	version("1.1.5", md5="dd554f2b9a5237d7aec370a42cd12494", url="https://cran.r-project.org/src/contrib/NADA2_1.1.5.tar.gz")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-envstats@2.4:", type=("build", "run"))
	depends_on("r-fitdistrplus", type=("build", "run"))
	depends_on("r-kendall", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))
	depends_on("r-nada", type=("build", "run"))
	depends_on("r-perm", type=("build", "run"))
	depends_on("r-survminer", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-cengam", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-coin", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
