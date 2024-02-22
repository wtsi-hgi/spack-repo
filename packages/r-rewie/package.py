# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRewie(RPackage):
	"""Data Preparation and Diagnostics for Random Effects Within
Estimator

	Diagnostics and data preparation for random effects within estimator, random effects 
    within-idiosyncratic estimator, between-within-idiosyncratic model, and cross-classified between model.
    Mundlak, Yair (1978) <doi:10.2307/1913646>.
    Hausman, Jeffrey (1978) <doi:10.2307/1913827>.
    Allison, Paul (2009) <doi:10.4135/9781412993869>.
    Neuhaus, J.M., and J. D. Kalbfleisch (1998) <doi:10.2307/3109770>.
	"""
	
	homepage = "https://github.com/sduxbury/rewie"
	cran = "rewie" 

	version("0.1.0", md5="de6c5b034fdb4e3ec1f36ba0d1e314a9")

	depends_on("r-rockchalk", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-plm", type=("build", "run"))
