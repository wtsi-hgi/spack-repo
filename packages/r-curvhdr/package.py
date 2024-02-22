# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCurvhdr(RPackage):
	"""Filtering of Flow Cytometry Samples

	Filtering, also known as gating, of flow cytometry samples using 
             the curvHDR method, which is described in Naumann, U., Luta, G. and 
             Wand, M.P. (2010) <DOI:10.1186/1471-2105-11-44>.
	"""
	
	cran = "curvHDR" 

	version("1.2-2", md5="a3a17f60070ef051c4960cf9d9bab652")

	depends_on("r-feature", type=("build", "run"))
	depends_on("r-geometry", type=("build", "run"))
	depends_on("r-hdrcde", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
	depends_on("r-misc3d", type=("build", "run"))
	depends_on("r-ptinpoly", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
