# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLgtdl(RPackage):
	"""A Set of Methods for Longitudinal Data Objects

	A very simple implementation of a class for 
	     longitudinal data.
	"""
	
	cran = "lgtdl" 

	version("1.1.5", md5="f4cc8e76d2bc6267f88389e9af594f68")

	depends_on("r@1.2:", type=("build", "run"))
