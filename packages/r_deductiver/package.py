# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeductiver(RPackage):
	"""Deductive Rational Method

	Apply the Deductive Rational Method to a monthly series of flow or precipitation data to fill in missing data. The method is as described in: Campos, D.F., (1984, ISBN:9686194444). 
	"""
	
	cran = "DeductiveR" 

	version("1.0.0", md5="e8e99efb1b04aff33745dfb8f45ab8bb")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
