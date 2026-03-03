# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrettyr(RPackage):
	"""Pretty Descriptive Stats

	Functions for conventionally formatting descriptive stats,
 reshaping data frames and formatting R output as HTML.
	"""
	
	cran = "prettyR" 

	version("2.2-3", md5="0a3019be75cb91a12805a90973a8c842")

