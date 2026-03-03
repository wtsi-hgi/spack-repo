# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGendata(RPackage):
	"""Generate and Modify Synthetic Datasets

	Set of functions to create datasets using a correlation matrix. 
	"""
	
	cran = "gendata" 

	version("1.2.0", md5="f989b8261b03786a48c54c5b9186219a")

