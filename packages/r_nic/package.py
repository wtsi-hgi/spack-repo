# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNic(RPackage):
	"""Nature Inspired Colours

	Color palettes based on nature inspired colours in "Sri Lanka".
	"""
	
	homepage = "https://github.com/thiyangt/nic"
	cran = "nic" 

	version("0.0.2", md5="bf73cffa471fb680264d92612bab7ab4")

