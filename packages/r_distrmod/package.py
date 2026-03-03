# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDistrmod(RPackage):
	"""Object Oriented Implementation of Probability Models

	Implements S4 classes for probability models based on packages 'distr' and
            'distrEx'.
	"""
	
	homepage = "http://distr.r-forge.r-project.org/"
	cran = "distrMod" 

	version("2.9.1", md5="da855b4fb26585c88f9379043c815632")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-distr@2.8:", type=("build", "run"))
	depends_on("r-distrex@2.8:", type=("build", "run"))
	depends_on("r-randvar@1.2:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-startupmsg", type=("build", "run"))
	depends_on("r-sfsmisc", type=("build", "run"))
