# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCorclass(RPackage):
	"""Correlational Class Analysis

	Perform a correlational class analysis of the data, resulting in a partition of the data into separate modules.
	"""
	
	cran = "corclass" 

	version("0.2.1", md5="a04b9478adf0f651faab30245349a107")

	depends_on("r-igraph", type=("build", "run"))
