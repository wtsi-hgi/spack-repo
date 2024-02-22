# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLorentz(RPackage):
	"""The Lorentz Transform in Relativistic Physics

	The Lorentz transform in special relativity; also the gyrogroup structure of three-velocities.  Includes active and passive transforms and the ability to use units in which the speed of light is not one.  For general relativity, see the
  'schwarzschild' package.
	"""
	
	homepage = "https://github.com/RobinHankin/lorentz"
	cran = "lorentz" 

	version("1.0-5", md5="7ff487e43f6980ebf26ea4936c0ffb35")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-emulator@1.2.20:", type=("build", "run"))
	depends_on("r-tensor", type=("build", "run"))
	depends_on("r-magic", type=("build", "run"))
