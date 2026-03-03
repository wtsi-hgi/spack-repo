# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REasyverification(RPackage):
	"""Ensemble Forecast Verification for Large Data Sets

	Set of tools to simplify application of atomic forecast
    verification metrics for (comparative) verification of ensemble forecasts
    to large data sets. The forecast metrics are imported from the
    'SpecsVerification' package, and additional forecast metrics are provided
    with this package. Alternatively, new user-defined forecast scores can be
    implemented using the example scores provided and applied using the
    functionality of this package.
	"""
	
	homepage = "https://www.meteoswiss.admin.ch"
	cran = "easyVerification" 

	version("0.4.5", md5="b72512db04cc1c57d140841a48a1c0d1")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-specsverification@0.5:", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
