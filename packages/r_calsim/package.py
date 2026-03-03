# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCalsim(RPackage):
	"""The Calibration Simplex

	Generates the calibration simplex (a generalization of the reliability diagram) for three-category probability forecasts, as proposed by Wilks (2013) <doi:10.1175/WAF-D-13-00027.1>.
	"""
	
	cran = "CalSim" 

	version("0.5.2", md5="f183b65cf8affc84090bb8ca8983f5e1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-spatstat@2.0.0:", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-exactmultinom", type=("build", "run"))
