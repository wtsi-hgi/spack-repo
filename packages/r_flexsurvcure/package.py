# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlexsurvcure(RPackage):
	"""Flexible Parametric Cure Models

	Flexible parametric mixture and non-mixture cure models for time-to-event data.
	"""
	
	homepage = "https://github.com/jrdnmdhl/flexsurvcure"
	cran = "flexsurvcure" 

	version("1.3.1", md5="3972aba9a32f47cadf37596d21e6baf4")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-flexsurv", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
