# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpcadjust(RPackage):
	"""Functions for Calibrating Control Charts

	Calibration of thresholds of control charts such as
    CUSUM charts based on past data, taking estimation error into account.
	"""
	
	cran = "spcadjust" 

	version("1.1", md5="5c8249c451f205fb1ab09402b67937fa")

	depends_on("r@2.5:", type=("build", "run"))
