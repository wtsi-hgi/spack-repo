# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLst(RPackage):
	"""Land Surface Temperature Retrieval for Landsat 8

	Calculates Land Surface Temperature from Landsat band 10 and 11.
  Revision of the Single-Channel Algorithm for Land Surface Temperature Retrieval From Landsat Thermal-Infrared Data. Jimenez-Munoz JC, Cristobal J, Sobrino JA, et al (2009). <doi: 10.1109/TGRS.2008.2007125>.
  Land surface temperature retrieval from LANDSAT TM 5. Sobrino JA, Jiménez-Muñoz JC, Paolini L (2004). <doi:10.1016/j.rse.2004.02.003>.
  Surface temperature estimation in Singhbhum Shear Zone of India using Landsat-7 ETM+ thermal infrared data. Srivastava PK, Majumdar TJ, Bhattacharya AK (2009). <doi: 10.1016/j.asr.2009.01.023>.
  Mapping land surface emissivity from NDVI: Application to European, African, and South American areas. Valor E (1996). <doi:10.1016/0034-4257(96)00039-9>.
  On the relationship between thermal emissivity and the normalized difference vegetation index for natural surfaces. Van de Griend AA, Owe M (1993). <doi:10.1080/01431169308904400>.
  Land Surface Temperature Retrieval from Landsat 8 TIRS—Comparison between Radiative Transfer Equation-Based Method, Split Window Algorithm and Single Channel Method. Yu X, Guo X, Wu Z (2014). <doi:10.3390/rs6109829>.
  Calibration and Validation of land surface temperature for Landsat8-TIRS sensor. Land product validation and evolution. Skoković D, Sobrino JA, Jimenez-Munoz JC, Soria G, Julien Y, Mattar C, Cristóbal J. (2014).
	"""
	
	cran = "LST" 

	version("1.1.0", md5="a14a2accbdc40efbd8d51ca11a939d4c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
