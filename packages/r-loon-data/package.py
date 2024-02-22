# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLoonData(RPackage):
	"""Data Used to Illustrate 'Loon' Functionality

	Data used as examples in the 'loon' package.
	"""
	
	homepage = "https://great-northern-diver.github.io/loon.data/"
	cran = "loon.data" 

	version("0.1.3", md5="fee28e2a5de5f2e94c4bd40980a2cf0b")

	depends_on("r@3.5:", type=("build", "run"))
