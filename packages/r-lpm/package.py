# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLpm(RPackage):
	"""Linear Parametric Models Applied to Hydrological Series

	Apply Univariate Long Memory Models,
    Apply Multivariate Short Memory Models To Hydrological Dataset,
    Estimate Intensity Duration Frequency curve to rainfall series.
	"""
	
	homepage = "http://www.corradotallerini.altervista.org/LPM.html"
	cran = "LPM" 

	version("2.9", md5="f495d0b1d302975145f4b747d2c65f55")

	depends_on("r-fracdiff", type=("build", "run"))
	depends_on("r-powdist", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
