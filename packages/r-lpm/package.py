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
    NEW -- Calculate the monthly water requirement for herbaceous and arboreal 
    plants.
	"""
	
	homepage = "http://www.corradotallerini.altervista.org/LPM.html"
	cran = "LPM" 

	version("3.0", md5="f85e6461046d2b41d025dbb0478c2a8a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-fracdiff", type=("build", "run"))
	depends_on("r-powdist", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
