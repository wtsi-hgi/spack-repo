# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRunstats(RPackage):
	"""Fast Computation of Running Statistics for Time Series

	Provides methods for fast computation of running sample 
    statistics for time series. These include: (1) mean, (2) 
    standard deviation, and (3) variance over a fixed-length window 
    of time-series, (4) correlation, (5) covariance, and (6) 
    Euclidean distance (L2 norm) between short-time pattern and 
    time-series. Implemented methods utilize Convolution Theorem to 
    compute convolutions via Fast Fourier Transform (FFT).
	"""
	
	homepage = "https://github.com/martakarass/runstats"
	cran = "runstats" 

	version("1.1.0", md5="5194f0795b566cbcb18b3d520372ad6a")

	depends_on("r-fftwtools", type=("build", "run"))
