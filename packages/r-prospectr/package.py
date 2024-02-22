# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProspectr(RPackage):
	"""Miscellaneous Functions for Processing and Sample Selection of
Spectroscopic Data

	Functions to preprocess spectroscopic data 
    and conduct (representative) sample selection/calibration sampling.
	"""
	
	homepage = "https://github.com/l-ramirez-lopez/prospectr"
	cran = "prospectr" 

	version("0.2.7", md5="c1208ada8f6d68898a4043ffd6536c2c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mathjaxr@1:", type=("build", "run"))
	depends_on("r-lifecycle@0.2:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
