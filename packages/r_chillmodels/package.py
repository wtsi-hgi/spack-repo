# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChillmodels(RPackage):
	"""Processing Chill and Heat Models for Temperate Fruit Trees

	Calculates the chilling and heat accumulation for studies of the temperate fruit trees. The models in this package are: Utah (Richardson et al., 1974, ISSN:0018-5345), Positive Chill Units - PCU (Linsley-Noaks et al., 1995, ISSN:1017-0316), GDH-A - Growing Degree Hours by Anderson et al.(1986, ISSN:0567-7572), GDH-R - Growing Degree Hours by Richardson et al.(1975, ISSN:0018-5345), North Carolina (Shaltout e Unrath, 1983, ISSN:0003-1062), Landsberg Model (Landsberg, 1974, ISSN:0305-7364), Q10 Model (Bidabe, 1967, ISSN:0031-9368), Jones Model (Jones et al., 2013 <DOI:10.1111/j.1438-8677.2012.00590.x>), Low-Chill Model (Gilreath and Buchanan, 1981, ISSN:0003-1062), Model for Cherry "Sweetheart" (Guak and Nielsen, 2013 <DOI:10.1007/s13580-013-0140-9>), Model for apple "Gala" (Guak and Nielsen, 2013 <DOI:10.1007/s13580-013-0140-9>), Taiwan Model (Lu et al., 2012 <DOI:10.17660/ActaHortic.2012.962.35>), Dynamic Model (Fishman et al., 1987, ISSN:0022-5193) adapted from the function Dynamic_Model() of the 'chillR' package (Luedeling, 2018), Unified Model (Chuine et al., 2016 <DOI:10.1111/gcb.13383>) and Heat Restriction model.
	"""
	
	cran = "ChillModels" 

	version("1.0.2", md5="ede5e6c471e4cb759f5071c8a927c6b1")

	depends_on("r@3.6:", type=("build", "run"))
