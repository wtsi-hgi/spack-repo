# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlugdensity(RPackage):
	"""Plug-in Kernel Density Estimation

	Kernel density estimation with global bandwidth selection
	     via "plug-in".
	"""
	
	homepage = "http://curves-etc.r-forge.r-project.org/"
	cran = "plugdensity" 

	version("0.8-5", md5="d37facc0969924f3bf29d73ef300d78a")

