# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMagiclamp(RPackage):
	"""'WeMo Switch' Smart Plug Utilities

	Set of utility functions to interact with 'WeMo Switch', a smart 
    plug that can be remotely controlled via wifi. The provided functions make 
    it possible to turn one or more 'WeMo Switch' plugs on and off in a 
    scriptable fashion. More information about 'WeMo Switch' can be found at 
    <http://www.belkin.com/us/p/P-F7C027/>. 
	"""
	
	homepage = "https://github.com/swarm-lab/magicLamp"
	cran = "magicLamp" 

	version("0.1.0", md5="efe0c7a1cc35b636cd1feec062f066e9")

	depends_on("r-httr@1.3.1:", type=("build", "run"))
	depends_on("r-tibble@1.3.4:", type=("build", "run"))
