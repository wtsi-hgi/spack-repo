# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDistrdoc(RPackage):
	"""Documentation for 'distr' Family of R Packages

	Provides documentation in form of a common vignette to packages 'distr',
            'distrEx', 'distrMod', 'distrSim', 'distrTEst', 'distrTeach', and 'distrEllipse'.
	"""
	
	homepage = "http://distr.r-forge.r-project.org/"
	cran = "distrDoc" 

	version("2.8.2", md5="ec6eda45d426637d788e20a931c28697")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-distr@2.2:", type=("build", "run"))
	depends_on("r-distrex@2.2:", type=("build", "run"))
	depends_on("r-distrsim@2.2:", type=("build", "run"))
	depends_on("r-distrtest@2.2:", type=("build", "run"))
	depends_on("r-distrteach@2.2:", type=("build", "run"))
	depends_on("r-randvar@0.7:", type=("build", "run"))
	depends_on("r-distrmod@2.2:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-startupmsg", type=("build", "run"))
