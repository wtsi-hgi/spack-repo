# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRconics(RPackage):
	"""Computations on Conics

	Solve some conic related problems (intersection of conics with lines and conics, arc length of an ellipse, polar lines, etc.). 
	"""
	
	homepage = "https://github.com/emanuelhuber/RConics"
	cran = "RConics" 

	version("1.1.1", md5="e319cefed78e6f6d84e34090934cae41")

	depends_on("r@2.10:", type=("build", "run"))
