# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPvaclone(RPackage):
	"""Population Viability Analysis with Data Cloning

	Likelihood based population viability analysis in the
  presence of observation error and missing data.
  The package can be used to fit, compare, predict,
  and forecast various growth model types using data cloning.
	"""
	
	homepage = "https://github.com/psolymos/PVAClone"
	cran = "PVAClone" 

	version("0.1-7", md5="ccfc5bd0d95d48a16a61fd3d2c5d2141")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-dcmle@0.3.0:", type=("build", "run"))
	depends_on("r-dclone", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("jags@3.0.0:", type=("build", "link", "run"))
