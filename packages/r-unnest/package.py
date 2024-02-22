# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUnnest(RPackage):
	"""Unnest Hierarchical Data Structures

	Fast flattening of hierarchical data structures (e.g. JSON, XML)
             into data.frames with a flexible spec language.
	"""
	
	homepage = "https://github.com/vspinu/unnest"
	cran = "unnest" 

	version("0.0.5", md5="5cecb5f63160e9846004fbc38ad662ac")

