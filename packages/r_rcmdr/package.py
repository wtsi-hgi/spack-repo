# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcmdr(RPackage):
	"""R Commander

	
  A platform-independent basic-statistics GUI (graphical user interface) for R, based on the tcltk package.
	"""
	
	homepage = "https://r-forge.r-project.org/projects/rcmdr/"
	cran = "Rcmdr" 

	version("2.9-2", md5="6b51f778cbadf2c4a6417e67080e9b12")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcmdrmisc@2.9.1:", type=("build", "run"))
	depends_on("r-car@3.1.0:", type=("build", "run"))
	depends_on("r-effects@4.0.3:", type=("build", "run"))
	depends_on("r-tcltk2@1.2.6:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-relimp@1.0.5:", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
