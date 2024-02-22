# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMopac(RPackage):
	"""Collection of Datasets Pertaining to Loop 1 "Mopac"

	Provides real & simulated datasets containing time-series traffic observations
    and additional information pertaining to Loop 1 "Mopac" located in Austin, Texas.
	"""
	
	homepage = "https://github.com/sccmckenzie/mopac"
	cran = "mopac" 

	version("0.1.0", md5="df5d983d88e6768135c5cefeb434b132")

	depends_on("r@2.10:", type=("build", "run"))
