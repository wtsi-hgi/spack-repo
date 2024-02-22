# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGarchx(RPackage):
	"""Flexible and Robust GARCH-X Modelling

	Flexible and robust estimation and inference of generalised autoregressive conditional heteroscedasticity (GARCH) models with covariates ('X') based on the results by Francq and Thieu (2018) <doi:10.1017/S0266466617000512>. Coefficients can straightforwardly be set to zero by omission, and quasi maximum likelihood methods ensure estimates are generally consistent and inference valid, even when the standardised innovations are non-normal and/or dependent over time, see <https://journal.r-project.org/archive/2021/RJ-2021-057/RJ-2021-057.pdf> for an overview of the package.
	"""
	
	homepage = "https://www.sucarrat.net/"
	cran = "garchx" 

	version("1.5", md5="07437a70f8081c7ed0ff08bae1499992")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
