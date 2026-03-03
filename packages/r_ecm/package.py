# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcm(RPackage):
	"""Build Error Correction Models

	Functions for easy building of error correction models (ECM) for time series regression. 
	"""
	
	homepage = "https://github.com/gaurbans/ecm"
	cran = "ecm" 

	version("7.2.0", md5="30b882661c46be59f1b7bc6d80b9099e")

	depends_on("r-car", type=("build", "run"))
	depends_on("r-earth", type=("build", "run"))
