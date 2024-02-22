# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHosm(RPackage):
	"""High Order Spatial Matrix

	Automatically displays the order and spatial weighting matrix of the distance between locations. This concept was derived from the research of Mubarak, Aslanargun, and Siklar (2021) <doi:10.52403/ijrr.20211150> and Mubarak, Aslanargun, and Siklar (2022) <doi:10.17654/0972361722052>. Distance data between locations can be imported from 'Ms. Excel', 'maps' package or created in 'R' programming directly. This package also provides 5 simulations of distances between locations derived from fictitious data, the 'maps' package, and from research by Mubarak, Aslanargun, and Siklar (2022) <doi:10.29244/ijsa.v6i1p90-100>.
	"""
	
	homepage = "https://github.com/mubarakfadhlul/hosm"
	cran = "hosm" 

	version("0.1.0", md5="82f5880cda7300595a382df0acf62c4b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
