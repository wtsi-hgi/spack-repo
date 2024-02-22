# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobextremes(RPackage):
	"""Optimally Robust Estimation for Extreme Value Distributions

	Optimally robust estimation for extreme value distributions using S4 classes and
            methods (based on packages 'distr', 'distrEx', 'distrMod', 'RobAStBase', and
            'ROptEst'); the underlying theoretic results can be found in Ruckdeschel and
            Horbenko, (2013 and 2012), doi{10.1080/02331888.2011.628022} and
            doi{10.1007/s00184-011-0366-4}.
	"""
	
	homepage = "https://r-forge.r-project.org/projects/robast/"
	cran = "RobExtremes" 

	version("1.3.0", md5="aab369b09cff4a71d7bd9849f2078ae3")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-distrmod@2.8:", type=("build", "run"))
	depends_on("r-roptest@1.2:", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-evd", type=("build", "run"))
	depends_on("r-robastrda", type=("build", "run"))
	depends_on("r-distr", type=("build", "run"))
	depends_on("r-distrex@2.8:", type=("build", "run"))
	depends_on("r-randvar", type=("build", "run"))
	depends_on("r-robastbase@1.2:", type=("build", "run"))
	depends_on("r-startupmsg", type=("build", "run"))
	depends_on("r-actuar", type=("build", "run"))
