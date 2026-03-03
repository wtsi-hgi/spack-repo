# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScorepeak(RPackage):
	"""Peak Functions for Peak Detection in Univariate Time Series

	Provides peak functions, which enable us to detect peaks in time series. The methods implemented in this package are based on Girish Keshav Palshikar (2009) <https://www.researchgate.net/publication/228853276_Simple_Algorithms_for_Peak_Detection_in_Time-Series>.
	"""
	
	homepage = "https://github.com/ShotaOchi/scorepeak"
	cran = "scorepeak" 

	version("0.1.2", md5="292a4899060cfab26cdb1fcc8e73fdec")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-checkmate@1.9.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
