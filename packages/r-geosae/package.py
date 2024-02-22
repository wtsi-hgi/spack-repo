# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeosae(RPackage):
	"""Geoadditive Small Area Model

	This function is an extension of the Small Area Estimation (SAE) model. Geoadditive Small Area Model is a combination of the geoadditive model with the Small Area Estimation (SAE) model, by adding geospatial information to the SAE model. This package refers to J.N.K Rao and Isabel Molina (2015, ISBN: 978-1-118-73578-7), Bocci, C., & Petrucci, A. (2016)<doi:10.1002/9781118814963.ch13>, and Ardiansyah, M., Djuraidah, A., & Kurnia, A. (2018)<doi:10.21082/jpptp.v2n2.2018.p101-110>.
	"""
	
	homepage = "https://github.com/ketutdika/geoSAE"
	cran = "geoSAE" 

	version("0.1.0", md5="9b43a4aad396428ba022a4e6adf39760")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
