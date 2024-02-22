# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLsd(RPackage):
	"""Lots of Superior Depictions

	Create lots of colorful plots in a plethora of variations. Try the LSD demotour().
	"""
	
	cran = "LSD" 

	version("4.1-0", md5="aac68db34a6deb2d4e788749a54a9594")

