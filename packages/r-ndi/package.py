# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNdi(RPackage):
	"""Neighborhood Deprivation Indices

	Computes various metrics of socio-economic deprivation and disparity in
             the United States. Some metrics are considered "spatial" because they 
             consider the values of neighboring (i.e., adjacent) census geographies in
             their computation, while other metrics are "aspatial" because they only 
             consider the value within each census geography. Two types of aspatial 
             neighborhood deprivation indices (NDI) are available: including:
             (1) based on Messer et al. (2006) <doi:10.1007/s11524-006-9094-x>
             and (2) based on Andrews et al. (2020) <doi:10.1080/17445647.2020.1750066> 
             and Slotman et al. (2022) <doi:10.1016/j.dib.2022.108002>
             who use variables chosen by Roux and Mair (2010)
             <doi:10.1111/j.1749-6632.2009.05333.x>. Both are a decomposition of multiple
             demographic characteristics from the U.S. Census Bureau American Community 
             Survey 5-year estimates (ACS-5; 2006-2010 onward). Using data from the ACS-5
             (2005-2009 onward), the package can also (1) compute the spatial Racial Isolation
             Index (RI) based on Anthopolos et al. (2011) <doi:10.1016/j.sste.2011.06.002>,
             (2) compute the spatial Educational Isolation Index (EI) based on Bravo et al.
             (2021) <doi:10.3390/ijerph18179384>, (3) compute the aspatial Index of 
             Concentration at the Extremes (ICE) based on Feldman et al. (2015) 
             <doi:10.1136/jech-2015-205728> and Krieger et al. (2016) 
             <doi:10.2105/AJPH.2015.302955>, (4) compute the aspatial racial/ethnic 
             Dissimilarity Index based on Duncan & Duncan (1955) <doi:10.2307/2088328>, (5)
             compute the aspatial income or racial/ethnic Atkinson Index based on Atkinson 
             (1970)  <doi:10.1016/0022-0531(70)90039-6>, (6) aspatial racial/ethnic Isolation
             Index (II) based on Shevky & Williams (1949; ISBN-13:978-0-837-15637-8) and Bell
             (1954) <doi:10.2307/2574118>, (7) aspatial racial/ethnic Correlation Ratio 
             based on Bell (1954) <doi:10.2307/2574118> and White (1986) <doi:10.2307/3644339>,
             (8) aspatial racial/ethnic Location Quotient (LQ) based on Merton (1939) 
             <doi:10.2307/2084686> and Sudano et al. (2013) 
             <doi:10.1016/j.healthplace.2012.09.015>, and (9) aspatial racial/ethnic Local
             Exposure and Isolation metric based on Bemanian & Beyer (2017) 
             <doi:10.1158/1055-9965.EPI-16-0926>. Also using data from the ACS-5 (2005-2009
             onward), the package can retrieve the aspatial Gini Index based Gini (1921)
             <doi:10.2307/2223319>.
	"""
	
	homepage = "https://github.com/idblr/ndi"
	cran = "ndi" 

	version("0.1.5", md5="52939aba432c23490bfff98d9a36a4d1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidycensus", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
