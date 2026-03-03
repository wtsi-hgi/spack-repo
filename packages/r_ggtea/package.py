# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgtea(RPackage):
	"""Palettes and Themes for 'ggplot2'

	A collection of palettes and themes for 'ggplot2', offering a light, pastel aesthetic. Syntax follows the 'viridis' package. 
	"""
	
	cran = "ggtea" 

	version("0.1.1", md5="717b71c309d8bfeabf5c621ea37fd6c1")

	depends_on("r-ggplot2", type=("build", "run"))
