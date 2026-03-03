# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCartogram(RPackage):
	"""Create Cartograms with R

	Construct continuous and non-contiguous area cartograms.
	"""
	
	homepage = "https://github.com/sjewo/cartogram"
	cran = "cartogram" 

	version("0.3.0", md5="da39177aebe36087d37d3f428c0325e9")

	depends_on("r-sf", type=("build", "run"))
	depends_on("r-packcircles", type=("build", "run"))
