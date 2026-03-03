# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGains(RPackage):
	"""Lift (Gains) Tables and Charts

	Constructs gains tables and lift charts for prediction algorithms. Gains tables and lift charts are commonly used in direct marketing applications.  The method is described in Drozdenko and Drake (2002), "Optimal Database Marketing", Chapter 11.
	"""
	
	cran = "gains" 

	version("1.2", md5="72dd78f27325b7fff825738e9c00b91b")

	depends_on("r@3:", type=("build", "run"))
