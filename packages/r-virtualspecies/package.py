# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVirtualspecies(RPackage):
	"""Generation of Virtual Species Distributions

	Provides a framework for generating virtual species distributions,
    a procedure increasingly used in ecology to improve species distribution
    models. This package integrates the existing methodological approaches 
    with the objective of generating virtual species distributions with 
    increased ecological realism.
	"""
	
	homepage = "https://borisleroy.com/virtualspecies/"
	cran = "virtualspecies" 

	version("1.6", md5="f1de9717d3dc9536dd3c9630192806e8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-ade4", type=("build", "run"))
	depends_on("r-rnaturalearth", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
