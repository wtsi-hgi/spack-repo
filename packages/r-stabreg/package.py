# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStabreg(RPackage):
	"""Linear Regression with the Stable Distribution

	Efficient regression for heavy-tailed and skewed data following a stable distribution. Generalized regression where the skewness and tail parameter of residuals are dependent on regressors is also available. Includes fast calculation of stable densities. Calculation of densities is based on efficient numerical methods from Ament and O'Neil (2017) <doi:10.1007/s11222-017-9725-y>. Parts of the code have been ported to C from Ament's 'Matlab' code available at <https://gitlab.com/s_ament/qastable>.
	"""
	
	cran = "stabreg" 

	version("0.1.2", md5="46ecd58d16a5af771fded741e8998dc4")

	depends_on("r-numderiv", type=("build", "run"))
