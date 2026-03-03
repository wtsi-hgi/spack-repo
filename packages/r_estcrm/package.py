# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REstcrm(RPackage):
	"""Calibrating Parameters for the Samejima's Continuous IRT Model

	Estimates item and person parameters for the Continuous Response Model (CRM; Samejima, 1973, <doi:10.1007/BF02291114>), computes item fit residual statistics, draws empirical 3D item category response curves, draws theoretical 3D item category response curves, and generates data under the CRM for simulation studies.
	"""
	
	homepage = "https://cengiz.me/"
	cran = "EstCRM" 

	version("1.6", md5="39ec98f5e3ea621c515e25c674373e2d")

	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
