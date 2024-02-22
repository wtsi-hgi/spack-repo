# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROhun(RPackage):
	"""Optimizing Acoustic Signal Detection

	Facilitates the automatic detection of acoustic signals, 
    providing functions to diagnose and optimize the performance of detection 
    routines. Detections from other software can also be explored and optimized.
    Araya-Salas et al. (2022) <doi:10.1101/2022.12.13.520253>.
	"""
	
	homepage = "https://docs.ropensci.org/ohun/"
	cran = "ohun" 

	version("1.0.1", md5="1af3cbab83e14c076f38119000cbac72")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-tuner", type=("build", "run"))
	depends_on("r-warbler@1.1.29:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-seewave@2.0.1:", type=("build", "run"))
	depends_on("r-fftw", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
