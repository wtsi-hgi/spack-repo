# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXrpython(RPackage):
	"""Structured Interface to 'Python'

	A 'Python' interface structured according to the general
    form described in package 'XR' and in the book "Extending R".
	"""
	
	cran = "XRPython" 

	version("0.8", md5="bf644da0869353500a7257b99495998e")

	depends_on("r-xr@0.7.1:", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
