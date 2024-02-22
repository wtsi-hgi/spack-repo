# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTagr(RPackage):
	"""Tagging and Organizing Objects in R

	
    Provides functions for attaching tags to R objects,
    searching for objects based on tags, and removing tags from objects.
    It also includes a function for removing all tags from an object, as well
    as a function for deleting all objects with a specific tag from the R
    environment. The package is useful for organizing and managing large
    collections of objects in R.
	"""
	
	homepage = "https://github.com/jsugarelli/tagr/"
	cran = "tagr" 

	version("1.0.1", md5="089d5045e566cb02fba6c5fa578d5405")

