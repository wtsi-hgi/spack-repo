# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXtal(RPackage):
	"""Crystallization Toolset

	This is the tool set for crystallographer to design and analyze crystallization experiments, especially for ribosome from Mycobacterium tuberculosis.
	"""
	
	cran = "xtal" 

	version("1.15", md5="62d9654238e8ee85b5faa166b09bc3f5")

