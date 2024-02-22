# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpt(RPackage):
	"""Sierpinski Pedal Triangle

	A collection of algorithms related to Sierpinski 
  pedal triangle (SPT).
	"""
	
	cran = "spt" 

	version("2.5.1", md5="7faa32a281a9f84f910ce98815bf248c")

