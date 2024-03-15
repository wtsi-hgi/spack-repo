# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXrjulia(RPackage):
	"""Structured Interface to Julia

	A Julia interface structured according to the general
	     form described in package 'XR' and in the book "Extending R".
	"""
	
	cran = "XRJulia" 

	version("0.9.0", md5="cb40c5173faf5494a5849bac545c7de5")

	depends_on("r-xr", type=("build", "run"))
	depends_on("julia@1.0:", type=("build", "link", "run"))
