# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFdth(RPackage):
	"""Frequency Distribution Tables, Histograms and Polygons

	Perform frequency distribution tables, associated histograms
             and polygons from vector, data.frame and matrix objects for
             numerical and categorical variables.
	"""
	
	homepage = "https://github.com/jcfaria/fdth"
	cran = "fdth" 

	version("1.3-0", md5="b6d929318864aedd91f6e55b4ee7232f")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
