# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRaverage(RPackage):
	"""Parameter Estimation for the Averaging Model of Information
Integration Theory

	Implementation of the R-Average method for parameter estimation of averaging models of the Anderson's Information Integration Theory by Vidotto, G., Massidda, D., & Noventa, S. (2010) <https://www.uv.es/psicologica/articulos3FM.10/3Vidotto.pdf>.
	"""
	
	cran = "rAverage" 

	version("0.5-8", md5="5c445d77e1c8415ef00f74873ea5fc3c")

	depends_on("r@2.8:", type=("build", "run"))
