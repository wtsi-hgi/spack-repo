# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStrucdiv(RPackage):
	"""Spatial Structural Diversity Quantification in Raster Data

	Spatial structural diversity refers to the spatial, i.e.
    horizontal arrangement of landscape elements and can reveal itself as
    landscape features, such as patches and linear features. The 'R' package
    'StrucDiv' provides methods to quantify spatial structural diversity
    in continuous remote sensing data, or in other data in raster format.
    Structure is based on the spatial arrangement of value pairs. The 'R' package 'StrucDiv'
    includes methods to combine information from different spatial scales, which allows to quantify
    multi-scale spatial structural diversity.
	"""
	
	homepage = "https://github.com/leilsc/StrucDiv"
	cran = "StrucDiv" 

	version("0.2.1", md5="66e7962625ceab08b4d5b838c9c69460")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-doparallel@1.0.15:", type=("build", "run"))
	depends_on("r-foreach@1.5:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-raster@3.1.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
