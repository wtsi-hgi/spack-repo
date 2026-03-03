# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcmdrpluginDoe(RPackage):
	"""R Commander Plugin for (Industrial) Design of Experiments

	Provides a platform-independent GUI for design of experiments.
 The package is implemented as a plugin to the R-Commander, which is a more general 
 graphical user interface for statistics in R based on tcl/tk. 
 DoE functionality can be accessed through the menu Design that is added to the 
 R-Commander menus.
	"""
	
	homepage = "https://prof.bht-berlin.de/groemping/DoE/"
	cran = "RcmdrPlugin.DoE" 

	version("0.12-5", md5="0aa9ff466c041dac06789478238d8027")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-doe-base@0.22.8:", type=("build", "run"))
	depends_on("r-frf2@1.2.10:", type=("build", "run"))
	depends_on("r-doe-wrapper@0.8.6:", type=("build", "run"))
	depends_on("r-rcmdr", type=("build", "run"))
	depends_on("r-rcmdrmisc", type=("build", "run"))
