# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlr3spatial(RPackage):
	"""Support for Spatial Objects Within the 'mlr3' Ecosystem

	Extends the 'mlr3' ML framework with methods for spatial
    objects. Data storage and prediction are supported for packages
    'terra', 'raster' and 'stars'.
	"""
	
	homepage = "https://mlr3spatial.mlr-org.com"
	cran = "mlr3spatial" 

	version("0.4.1", md5="2e2cdf4a1d4f382b3621f8e0aceb5bf2")

	depends_on("r-mlr3@0.14:", type=("build", "run"))
	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-checkmate@2:", type=("build", "run"))
	depends_on("r-data-table@1.14:", type=("build", "run"))
	depends_on("r-lgr@0.4.2:", type=("build", "run"))
	depends_on("r-mlr3misc@0.11:", type=("build", "run"))
	depends_on("r-r6@2.5:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-terra@1.6.3:", type=("build", "run"))
