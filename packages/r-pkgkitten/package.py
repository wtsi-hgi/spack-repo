# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPkgkitten(RPackage):
	"""Create Simple Packages Which Do not Upset R Package Checks

	Provides a function kitten() which creates cute little 
 packages which pass R package checks. This sets it apart from 
 package.skeleton() which it calls, and which leaves imperfect files 
 behind. As this is not exactly helpful for beginners, kitten() offers 
 an alternative. Unit test support can be added via the 'tinytest'
 package (if present), and documentation-creation support can be
 added via 'roxygen2' (if present).
	"""
	
	homepage = "https://github.com/eddelbuettel/pkgkitten"
	cran = "pkgKitten" 

	version("0.2.3", md5="7b58fad3ab4be2ad5ca3853c34c29f8b")

