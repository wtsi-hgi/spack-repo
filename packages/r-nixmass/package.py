# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNixmass(RPackage):
	"""Snow Water Equivalent Modeling with the 'Delta.snow' Model and
Empirical Regression Models

	Snow water equivalent is modeled with the process based 'delta.snow' model and empirical regression models using relationships between density and diverse at-site parameters. The methods are described in Winkler et al. (2021) <doi:10.5194/hess-25-1165-2021>, Guyennon et al. (2019) <doi:10.1016/j.coldregions.2019.102859>, Pistocchi (2016) <doi:10.1016/j.ejrh.2016.03.004>, Jonas et al. (2009) <doi:10.1016/j.jhydrol.2009.09.021> and Sturm et al. (2010) <doi:10.1175/2010JHM1202.1>.
	"""
	
	cran = "nixmass" 

	version("1.0.2", md5="5b6bd09f3533cdd3cf45231eec3c9c81")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
