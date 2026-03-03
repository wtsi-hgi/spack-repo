# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTwdtw(RPackage):
	"""Time-Weighted Dynamic Time Warping

	Implements Time-Weighted Dynamic Time Warping (TWDTW), 
    a measure for quantifying time series similarity. The TWDTW algorithm, 
    described in Maus et al. (2016) <doi:10.1109/JSTARS.2016.2517118> and 
    Maus et al. (2019) <doi:10.18637/jss.v088.i05>, is applicable to multi-dimensional 
    time series of various resolutions. It is particularly suitable for comparing 
    time series with seasonality for environmental and ecological data analysis, 
    covering domains such as remote sensing imagery, climate data, hydrology, 
    and animal movement. The 'twdtw' package offers a user-friendly 'R' interface, 
    efficient 'Fortran' routines for TWDTW calculations, flexible time weighting 
    definitions, as well as utilities for time series preprocessing and visualization.
	"""
	
	homepage = "https://github.com/vwmaus/twdtw/"
	cran = "twdtw" 

	version("1.0-1", md5="8e87bbbe46f77b9fd36d8cae1ed80b62")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-proxy", type=("build", "run"))
