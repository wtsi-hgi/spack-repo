# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMuchpoint(RPackage):
	"""Multiple Change Point

	Nonparametric approach to estimate the location of block boundaries (change-points) of 
    non-overlapping blocks in a random symmetric matrix which consists of random variables whose 
    distribution changes from block to block.
    BRAULT Vincent, OUADAH Sarah, SANSONNET Laure and LEVY-LEDUC Celine (2017) <doi:10.1016/j.jmva.2017.12.005>.
	"""
	
	homepage = "https://github.com/Lionning/MuChPoint"
	cran = "MuChPoint" 

	version("0.6.3", md5="4855697b2476f078fe7b5a8ad60c14ae")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-capushe", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
