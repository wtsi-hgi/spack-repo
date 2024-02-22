# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProftools(RPackage):
	"""Profile Output Processing Tools for R

	Tools for examining Rprof profile output.
	"""
	
	cran = "proftools" 

	version("0.99-3", md5="d37a9164123380f5ad571d73216ff967")

