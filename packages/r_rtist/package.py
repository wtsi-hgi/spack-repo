# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtist(RPackage):
	"""A Color Palette Generator

	Color palettes from famous artists and paintings.
	"""
	
	cran = "rtist" 

	version("1.0.0", md5="ec07816d331e652d1bc18dc9ae6b7145")

