# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSta(RPackage):
	"""Seasonal Trend Analysis for Time Series Imagery in R

	Efficiently estimate shape parameters of periodic time series 
    imagery with which  a statistical seasonal trend analysis (STA) is subsequently performed. 
    STA output can be exported in conventional raster formats. 
    Methods to visualize STA output are also implemented as well as the calculation 
    of additional basic statistics. STA is based on (R. Eastman, F. Sangermano, 
    B. Ghimire, H. Zhu, H. Chen, N. Neeti, Y. Cai, E. Machado and S. Crema, 2009) <doi:10.1080/01431160902755338>.
	"""
	
	cran = "sta" 

	version("0.1.7", md5="4f756a892da4f1bc0bc1a1f3b01b11e0")

	depends_on("r-raster@2.9.5:", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-geots@0.1.1:", type=("build", "run"))
	depends_on("r-foreach@1.4.4:", type=("build", "run"))
	depends_on("r-trend@1.1.1:", type=("build", "run"))
	depends_on("r-doparallel@1.0.14:", type=("build", "run"))
	depends_on("r-mapview@2.7:", type=("build", "run"))
	depends_on("r-rcolorbrewer@1.1.2:", type=("build", "run"))
