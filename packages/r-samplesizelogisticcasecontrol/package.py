# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSamplesizelogisticcasecontrol(RPackage):
	"""Sample Size and Power Calculations for Case-Control Studies

	To determine sample size or power for case-control studies to be analyzed using logistic regression.
	"""
	
	cran = "samplesizelogisticcasecontrol" 

	version("2.0.2", md5="2bfaa8b7b43db49ff9eb8482d2cb15a6")

	depends_on("r-mvtnorm", type=("build", "run"))
