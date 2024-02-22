# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUnicol(RPackage):
	"""The Colors of your University

	Most universities use specific color combinations to express their unique brand identity. The 'unicol' package provides the colors and color palettes of various universities for easy plotting and printing in R. We collect and provide a diverse range of color palettes for creating scientific visualizations. 
	"""
	
	homepage = "https://github.com/hneth/unicol/"
	cran = "unicol" 

	version("0.2.0", md5="61511e31b3045f2e003459d9544f4ed1")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-unikn", type=("build", "run"))
