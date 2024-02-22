# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcarus(RPackage):
	"""Calibrates and Reweights Units in Samples

	Provides user-friendly tools for calibration in survey sampling.
    The package is production-oriented, and its interface is inspired by the famous
    popular macro 'Calmar' for SAS, so that 'Calmar' users can quickly get used to
    'icarus'. In addition to calibration (with linear, raking and logit methods),
    'icarus' features functions for calibration on tight bounds and penalized
    calibration.
	"""
	
	cran = "icarus" 

	version("0.3.2", md5="4417b09018cec991f7bb7a123808caf7")

	depends_on("r@3.1.1:", type=("build", "run"))
