# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTempdisagg(RPackage):
	"""Methods for Temporal Disaggregation and Interpolation of Time
Series

	Temporal disaggregation methods are used to disaggregate and
    interpolate a low frequency time series to a higher frequency series, where
    either the sum, the mean, the first or the last value of the resulting
    high frequency series is consistent with the low frequency series. Temporal
    disaggregation can be performed with or without one or more high frequency
    indicator series. Contains the methods of Chow-Lin, Santos-Silva-Cardoso,
    Fernandez, Litterman, Denton and Denton-Cholette, summarized in Sax and
    Steiner (2013) <doi:10.32614/RJ-2013-028>. Supports most R time series
    classes.
	"""
	
	homepage = "https://journal.r-project.org/archive/2013-2/sax-steiner.pdf"
	cran = "tempdisagg" 

	version("1.1.1", md5="a10c05099510b9a4bb444024dc87e56a")

