# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpmg(RPackage):
	"""Graphical User Interface (GUI) for Interactive R Analysis
Sessions

	Really Poor Man's Graphical User Interface, used to create interactive R analysis sessions with simple R commands.
	"""
	
	cran = "RPMG" 

	version("2.2-7", md5="e2d6622e786f2704235fc960d6efd6f0")

