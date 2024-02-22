# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFrequencyconnectedness(RPackage):
	"""Spectral Decomposition of Connectedness Measures

	Accompanies a paper (Barunik, Krehlik (2018) <doi:10.1093/jjfinec/nby001>) dedicated to spectral decomposition of connectedness measures and their interpretation. We implement all the developed estimators as well as the historical counterparts. For more information, see the help or GitHub page (<https://github.com/tomaskrehlik/frequencyConnectedness>) for relevant information.
	"""
	
	homepage = "https://github.com/tomaskrehlik/frequencyConnectedness"
	cran = "frequencyConnectedness" 

	version("0.2.4", md5="9cd00266af03804a47059bf93befd1e5")

	depends_on("r-vars", type=("build", "run"))
	depends_on("r-urca", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
