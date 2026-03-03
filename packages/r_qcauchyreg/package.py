# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQcauchyreg(RPackage):
	"""Quantile Regression Quasi-Cauchy

	Quasi-Cauchy quantile regression, proposed by de Oliveira, Ospina, Leiva, Figueroa-Zuniga and Castro (2023) <doi:10.3390/fractalfract7090667>. This regression model is useful for the case where you want to model data of a nature limited to the intervals [0,1], (0,1], [0,1) or (0,1) and you want to use a quantile approach.
	"""
	
	homepage = "<https://www.r-project.org>"
	cran = "qcauchyreg" 

	version("1.0", md5="e77affe47f2e9dec80abeae073936b85")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
