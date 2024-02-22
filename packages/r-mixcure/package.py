# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMixcure(RPackage):
	"""Mixture Cure Models

	Implementation of parametric and semiparametric mixture cure models based on existing R packages. See details of the models in Peng and Yu (2020) <ISBN: 9780367145576>.
	"""
	
	cran = "mixcure" 

	version("2.0", md5="0edaf8cb722bd19b8a25c164f28f9378")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-flexsurv", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
	depends_on("r-gam", type=("build", "run"))
	depends_on("r-timereg", type=("build", "run"))
