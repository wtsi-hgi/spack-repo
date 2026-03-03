# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFhdi(RPackage):
	"""Fractional Hot Deck and Fully Efficient Fractional Imputation

	Impute general multivariate missing data with the fractional hot deck imputation based on Jaekwang Kim (2011) <doi:10.1093/biomet/asq073>.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "FHDI" 

	version("1.4.1", md5="f1115549191bd6904ae4d43465dc5311")

	depends_on("r@3.4:", type=("build", "run"))
