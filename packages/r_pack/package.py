# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPack(RPackage):
	"""Convert values to/from raw vectors

	Functions to easily convert data to binary formats other programs/machines can understand.
	"""
	
	cran = "pack" 

	version("0.1-1", md5="7800c9898bf6cc82b6b9faeb74ef097b")

