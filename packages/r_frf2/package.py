# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFrf2(RPackage):
	"""Fractional Factorial Designs with 2-Level Factors

	Regular and non-regular Fractional Factorial 2-level designs 
        can be created. Furthermore, analysis tools for Fractional
        Factorial designs with 2-level factors are offered (main
        effects and interaction plots for all factors simultaneously,
        cube plot for looking at the simultaneous effects of three
        factors, full or half normal plot, alias structure in a more
        readable format than with the built-in function alias). 
	"""
	
	homepage = "https://prof.bht-berlin.de/groemping/DoE/"
	cran = "FrF2" 

	version("2.3-3", md5="fa00a9fd2ea601c227288fb7699cf92d", url="https://cran.r-project.org/src/contrib/FrF2_2.3-3.tar.gz")

	depends_on("r@2.13:", type=("build", "run"))
	depends_on("r-doe-base@0.25:", type=("build", "run"))
	depends_on("r-sfsmisc@1.0.26:", type=("build", "run"))
	depends_on("r-scatterplot3d", type=("build", "run"))
	depends_on("r-igraph@0.7:", type=("build", "run"))
