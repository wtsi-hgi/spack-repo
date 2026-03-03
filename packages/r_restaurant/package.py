# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRestaurant(RPackage):
	"""Restaurant Data for Entity Resolution

	Duplicated restaurant data (pre-processed and formatted) for entity resolution. This package contains formatted data from a data set that contains information about different restaurants, with the Zagats portion containing 331 records and the Fodors portion containing 533 records. The following variables are included in the data set: id, name, address, city, phone, type. The data set has a respective gold data set that provides information on which records match based on id. 
	"""
	
	homepage = "https://github.com/resteorts/restaurant"
	cran = "restaurant" 

	version("0.1.0", md5="ea05515a4f127d8f8de5fbce92ea1900")

	depends_on("r@3.4:", type=("build", "run"))
