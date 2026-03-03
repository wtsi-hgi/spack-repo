# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWxgenr(RPackage):
	"""A Stochastic Weather Generator with Seasonality

	A weather generator to simulate precipitation and temperature for regions with seasonality. Users input training data containing precipitation, temperature, and seasonality (up to 20 seasons). Including weather season as a training variable allows users to explore the effects of potential changes in season duration as well as average start- and end-time dates due to phenomena like climate change. Data for training should be a single time series but can originate from station data, basin averages, grid cells, etc.
    Bearup, L., Gangopadhyay, S., & Mikkelson, K. (2021). "Hydroclimate Analysis Lower Santa Cruz River Basin Study (Technical Memorandum No ENV-2020-056)." Bureau of Reclamation. <https://www.usbr.gov/lc/phoenix/programs/lscrbasin/LSCRBS_Hydroclimate_2021.pdf>.
    Gangopadhyay, S., Bearup, L. A., Verdin, A., Pruitt, T., Halper, E., & Shamir, E. (2019, December 1). "A collaborative stochastic weather generator for climate impacts assessment in the Lower Santa Cruz River Basin, Arizona." Fall Meeting 2019, American Geophysical Union. <https://ui.adsabs.harvard.edu/abs/2019AGUFMGC41G1267G>.
	"""
	
	cran = "wxgenR" 

	version("1.3.6", md5="1df4bb227d5f9cb3686a2547d2cee673")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
	depends_on("r-sm", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
