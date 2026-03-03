# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCommonmeanCopula(RPackage):
	"""Common Mean Vector under Copula Models

	Estimate bivariate common mean vector under copula models with known correlation. In the current version, available copulas are the Clayton, Gumbel, Frank, Farlie-Gumbel-Morgenstern (FGM), and normal copulas. See Shih et al. (2019) <doi:10.1080/02331888.2019.1581782> and Shih et al. (2021) <under review> for details under the FGM and general copulas, respectively.
	"""
	
	cran = "CommonMean.Copula" 

	version("1.0.4", md5="3cbec6a5ab68eaf59cbb30fa21edee55")

	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
