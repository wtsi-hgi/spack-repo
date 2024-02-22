# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFeatures(RPackage):
	"""Feature Extraction for Discretely-Sampled Functional Data

	Discretely-sampled function is first smoothed.  Features
        of the smoothed function are then extracted.  Some of the key
        features include mean value, first and second derivatives,
        critical points (i.e. local maxima and minima), curvature of
        cunction at critical points, wiggliness of the function, noise
        in data, and outliers in data.
	"""
	
	homepage = "http://www.jhsph.edu/agingandhealth/People/Faculty_personal_pages/Varadhan.html"
	cran = "features" 

	version("2015.12-1", md5="72279bdadeb199e26164c6955186be72")

	depends_on("r-lokern", type=("build", "run"))
