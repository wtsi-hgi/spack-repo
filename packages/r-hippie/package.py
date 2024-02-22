# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHippie(RPackage):
	"""Hippie Code Completion in 'RStudio'

	An 'RStudio' Addin for Hippie Expand (AKA Hippie Code
  Completion or Cyclic Expand Word). This type of completion searches for 
  matching tokens within the user's current source editor file, regardless of
  file type. By searching only within the current source file, 'hippie' offers a
  fast way to identify and insert completions that appear around the user's
  cursor.
	"""
	
	homepage = "https://github.com/crew102/hippie"
	cran = "hippie" 

	version("0.1.0", md5="a48fceaa01b3d993747cd1e9252f4c22")

	depends_on("r-rstudioapi@0.13:", type=("build", "run"))
	depends_on("r-sourcetools", type=("build", "run"))
