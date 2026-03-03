# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRedmonder(RPackage):
	"""Microsoft(r)-Inspired Color Palettes

	Provide color schemes for maps (and other graphics) based on the
    color palettes of several Microsoft(r) products. Forked from 'RColorBrewer' v1.1-2.
	"""
	
	cran = "Redmonder" 

	version("0.2.0", md5="b1e310beb4156e3021e982e112a38839")

	depends_on("r@2:", type=("build", "run"))
