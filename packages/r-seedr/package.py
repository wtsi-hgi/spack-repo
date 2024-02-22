# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeedr(RPackage):
	"""Hydro and Thermal Time Seed Germination Models in R

	Analysis of seed germination data
    using the physiological time modelling approach. Includes functions
    to fit hydrotime and thermal-time models with the traditional approaches
    of Bradford (1990) <doi:10.1104/pp.94.2.840>
    and Garcia-Huidobro (1982) <doi:10.1093/jxb/33.2.288>. 
    Allows to fit models to grouped datasets,
    i.e. datasets containing multiple species, seedlots or experiments.
	"""
	
	homepage = "https://github.com/efernandezpascual/seedr"
	cran = "seedr" 

	version("0.3.0", md5="381bef3309aa14ba72e5036b588580d0")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-data-table@1.13:", type=("build", "run"))
	depends_on("r-binom@1.1:", type=("build", "run"))
