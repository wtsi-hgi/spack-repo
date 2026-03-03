# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAbundant(RPackage):
	"""High-Dimensional Principal Fitted Components and Abundant
Regression

	Fit and predict with the high-dimensional principal fitted
        components model.  This model is described by Cook, Forzani, and Rothman (2012)
	<doi:10.1214/11-AOS962>.
	"""
	
	cran = "abundant" 

	version("1.2", md5="e3e0bb3446cb849bb89ea47e49d6b923")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-glasso", type=("build", "run"))
