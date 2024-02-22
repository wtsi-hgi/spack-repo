# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSinaplot(RPackage):
	"""An Enhanced Chart for Simple and Truthful Representation of
Single Observations over Multiple Classes

	The sinaplot is a data visualization chart suitable for plotting
    any single variable in a multiclass data set. It is an enhanced jitter strip
    chart, where the width of the jitter is controlled by the density
    distribution of the data within each class.
	"""
	
	cran = "sinaplot" 

	version("1.1.0", md5="e0b0e8cf0b12f5e8560e90a09d77b473")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-plyr@1.8.4:", type=("build", "run"))
