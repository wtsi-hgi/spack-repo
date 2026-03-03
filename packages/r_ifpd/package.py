# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIfpd(RPackage):
	"""Indonesia Food Prices Data

	Imputation of missing values using the last observation carried forward technique on Indonesia food prices data that is time series data. Also, this technique applies imputation to data whose dates do not appear directly. So that the series assumptions in the time series data are met.
	"""
	
	homepage = "https://github.com/mubarakfadhlul/ifpd"
	cran = "ifpd" 

	version("0.1.0", md5="a5ea16102024c3f4a3831febc5d83bff")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
