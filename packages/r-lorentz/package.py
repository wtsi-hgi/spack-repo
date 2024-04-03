# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLorentz(RPackage):
	"""The Lorentz Transform in Relativistic Physics

	The Lorentz transform in special relativity; also the
    gyrogroup structure of three-velocities.  Performs active and
    passive transforms and has the ability to use units in which the
    speed of light is not unity.  Includes some experimental
    functionality for celerity and rapidity.  For general relativity,
    see the 'schwarzschild' package.
	"""
	
	homepage = "https://github.com/RobinHankin/lorentz"
	cran = "lorentz" 

	version("1.1-1", md5="d05d202df0b000935486a1dff936c2eb")

	depends_on("r-emulator@1.2.20:", type=("build", "run"))
	depends_on("r-tensor", type=("build", "run"))
	depends_on("r-magic", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
