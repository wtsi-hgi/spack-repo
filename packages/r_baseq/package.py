# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBaseq(RPackage):
	"""Basic Sequence Processing Tool for Biological Data

	Primarily created as an easy and understanding way to do basic sequences surrounding the central dogma of molecular biology.
	"""
	
	homepage = "https://github.com/ambuvjyn/baseq"
	cran = "baseq" 

	version("0.1.4", md5="b6672ad3c68aab7a5ace2c680f863292")

