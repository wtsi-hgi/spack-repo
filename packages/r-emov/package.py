# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmov(RPackage):
	"""Eye Movement Analysis Package for Fixation and Saccade Detection

	Fixation and saccade detection in eye movement recordings. This package implements a dispersion-based algorithm (I-DT) proposed by Salvucci & Goldberg (2000) which detects fixation duration and position.
	"""
	
	homepage = "https://github.com/schw4b/emov"
	cran = "emov" 

	version("0.1.1", md5="0ae51d87ae4f026e9b48aba4e8ccc1b4")

	depends_on("r@1.8:", type=("build", "run"))
