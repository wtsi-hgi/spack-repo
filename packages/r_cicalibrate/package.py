# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCicalibrate(RPackage):
	"""Calibration of Confidence Intervals to Support Intervals

	Provides functionality for computing support intervals for univariate parameters based on confidence intervals or parameter estimates with standard errors (Pawel et al., 2022) <doi:10.48550/arXiv.2206.12290>.
	"""
	
	homepage = "https://github.com/SamCH93/ciCalibrate"
	cran = "ciCalibrate" 

	version("0.42.2", md5="7e248f13fa28ce8542882d476c8b6606")

	depends_on("r-lamw", type=("build", "run"))
