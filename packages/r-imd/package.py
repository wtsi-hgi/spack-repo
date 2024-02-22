# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImd(RPackage):
	"""Index of Multiple Deprivation Data for the UK

	Index of Multiple Deprivation for UK nations at various 
    geographical levels. In England, deprivation data is for Lower Layer Super
    Output Areas, Middle Layer Super Output Areas, Wards, and Local Authorities
    based on data from <https://www.gov.uk/government/statistics/english-indices-of-deprivation-2019>.
    In Wales, deprivation data is for Lower Layer Super Output Areas, Middle 
    Layer Super Output Areas, Wards, and Local Authorities based on data from
    <https://gov.wales/welsh-index-multiple-deprivation-full-index-update-ranks-2019>.
    In Scotland, deprivation data is for Data Zones, Intermediate Zones, and 
    Council Areas based on data from <https://simd.scot>. In Northern Ireland,
    deprivation data is for Super Output Areas and Local Government Districts
    based on data from <https://www.nisra.gov.uk/statistics/deprivation/northern-ireland-multiple-deprivation-measure-2017-nimdm2017>.
    The 'IMD' package also provides the composite UK index developed by
    <https://github.com/mysociety/composite_uk_imd>.
	"""
	
	homepage = "https://github.com/humaniverse/IMD"
	cran = "IMD" 

	version("1.2.2", md5="d838dbc72203da56dbe2d85429b57503")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
