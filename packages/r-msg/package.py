# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsg(RPackage):
	"""Data and Functions for the Book Modern Statistical Graphics

	A companion to the Chinese book ``Modern Statistical Graphics''.
	"""
	
	homepage = "https://github.com/yihui/MSG"
	cran = "MSG" 

	version("0.8", md5="96101d25a10f21e1a3e0adbed439350d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcolorbrewer@1.1.2:", type=("build", "run"))
