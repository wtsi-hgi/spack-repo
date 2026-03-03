# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMtest(RPackage):
	"""A Procedure for Multicollinearity Testing using Bootstrap

	Functions for detecting multicollinearity. This test gives statistical support to two of the most famous methods for detecting multicollinearity in applied work: Klein’s rule and Variance Inflation Factor (VIF). See the URL for the papers associated with this package, as for instance, Morales-Oñate and Morales-Oñate (2015) <doi:10.33333/rp.vol51n2.05>.
	"""
	
	homepage = "https://github.com/vmoprojs/MTest"
	cran = "MTest" 

	version("1.0.2", md5="66ffb80637608801a6995ed554a1646b")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
