# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetasdtreg(RPackage):
	"""Regression Models for Meta Signal Detection Theory

	Regression methods for the meta-SDT model. The package implements methods for cognitive experiments of metacognition as described in Kristensen, S. B., Sandberg, K., & Bibby, B. M. (2020). Regression methods for metacognitive sensitivity. Journal of Mathematical Psychology, 94. <doi:10.1016/j.jmp.2019.102297>.
	"""
	
	cran = "metaSDTreg" 

	version("0.2.2", md5="1875afc7345eedf296e31af248bf49e3")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-ordinal@2022.11.16:", type=("build", "run"))
	depends_on("r-maxlik@1.5.2:", type=("build", "run"))
	depends_on("r-truncnorm@1.0.8:", type=("build", "run"))
	depends_on("r-matrix@1.4:", type=("build", "run"))
