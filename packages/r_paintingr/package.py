# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPaintingr(RPackage):
	"""Painting Palettes Generator

	Color palettes generated from paintings.
	"""
	
	cran = "paintingr" 

	version("0.1.0", md5="1c9e949fe08be03d6406101f2d151d3e")

