# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimile(RPackage):
	"""Interact with Simile Models

	Allows a Simile model saved as a compiled binary to be
  loaded, parameterized, executed and interrogated. This version works 
  with Simile v5.97 on.
	"""
	
	cran = "Simile" 

	version("1.3.3", md5="813858614a8fd41a8821db730c7fd134")

