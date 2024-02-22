# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGsbdesign(RPackage):
	"""Group Sequential Bayes Design

	Group Sequential Operating Characteristics for Clinical,
        Bayesian two-arm Trials with known Sigma and Normal Endpoints,
	as described in Gerber and Gsponer (2016) <doi: 10.18637/jss.v069.i11>.
	"""
	
	cran = "gsbDesign" 

	version("1.0-3", md5="f71075d305a0325f4d395e2e213a7991")

	depends_on("r-gsdesign", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
