# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrone(RPackage):
	"""Structural Crystallography in 1d

	Functions to carry out the most important crystallographic calculations for crystal 
             structures made of 1d Gaussian-shaped atoms, especially useful for methods development.
             Main reference: E. Smith, G. Evans, J. Foadi (2017) <doi:10.1088/1361-6404/aa8188>.
	"""
	
	cran = "crone" 

	version("0.1.1", md5="3ea42c7dae069dddd6d8dca17182a129")

	depends_on("r@3.5:", type=("build", "run"))
