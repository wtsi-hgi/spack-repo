# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGghist(RPackage):
	"""Plot the Histogram of a Numeric Vector

	Wrapper around geom_histogram() of 'ggplot2' to plot the histogram of a numeric vector. This is especially useful, since qplot() was deprecated in 'ggplot2' 3.4.0.
	"""
	
	homepage = "https://github.com/frederikziebell/gghist"
	cran = "gghist" 

	version("0.1.0", md5="4d40eb880dc8ab9e151f52dccaad1434")

	depends_on("r-ggplot2", type=("build", "run"))
