# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgcxgc(RPackage):
	"""Preprocessing and Multivariate Analysis of Bidimensional Gas
Chromatography Data

	Toolbox for chemometrics analysis of bidimensional gas 
    chromatography data. This package import data for common scientific data
    format (NetCDF) and fold it to 2D chromatogram. Then, it can perform
    preprocessing and multivariate analysis. In the preprocessing algorithms,
    baseline correction, smoothing, and peak alignment are available.
    While in multivariate analysis, multiway principal component analysis is
    incorporated.
	"""
	
	homepage = "https://github.com/DanielQuiroz97/RGCxGC"
	cran = "RGCxGC" 

	version("1.2.0", md5="b6eb69903e08eb11911094d8642c252d")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-rnetcdf", type=("build", "run"))
	depends_on("r-ptw", type=("build", "run"))
	depends_on("r-colorramps", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
