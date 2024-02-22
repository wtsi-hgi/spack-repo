# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDigitize(RPackage):
	"""Use Data from Published Plots in R

	Import data from a digital image; it requires user input for
    calibration and to locate the data points. The end result is similar to
    'DataThief' and other other programs that 'digitize' published plots or
    graphs.
	"""
	
	homepage = "https://github.com/tpoisot/digitize/"
	cran = "digitize" 

	version("0.0.4", md5="13f67aded3ac2d5a4090a58dc055b650")

	depends_on("r@2.2:", type=("build", "run"))
	depends_on("r-readbitmap@0.1.4:", type=("build", "run"))
