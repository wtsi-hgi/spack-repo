# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdvbinomapps(RPackage):
	"""Upper Clopper-Pearson Confidence Limits for Burn-in Studies
under Additional Available Information

	Functions to compute upper Clopper-Pearson confidence limits of early life failure probabilities and required sample sizes of burn-in studies under further available information, e.g. from other products or technologies. 
	"""
	
	cran = "AdvBinomApps" 

	version("1.0", md5="3709dad2d8a224c0ac712cf369916b1c")

	depends_on("r-genbinomapps", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
