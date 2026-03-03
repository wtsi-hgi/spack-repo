# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpaleoclim(RPackage):
	"""Download Paleoclimate Data from 'PaleoClim'

	
    'PaleoClim' <http://www.paleoclim.org> (Brown et al. 2019, 
  <doi:10.1038/sdata.2018.254>) is a set of free, high resolution paleoclimate 
  surfaces covering the whole globe. It includes data on surface temperature,
  precipitation and the standard bioclimatic variables commonly used in 
  ecological modelling, derived from the 'HadCM3' general circulation model and 
  downscaled to a spatial resolution of up to 2.5 minutes. Simulations are
  available for key time periods from the Late Holocene to mid-Pliocene. Data on
  current and Last Glacial Maximum climate is derived from 'CHELSA'  (Karger et 
  al. 2017, <doi:10.1038/sdata.2017.122>) and reprocessed by 'PaleoClim' to 
  match their format; it is available at up to 30 seconds resolution. This 
  package provides a simple interface for downloading 'PaleoClim' data in R, 
  with support for caching and filtering retrieved data by period, resolution,
  and geographic extent.
	"""
	
	homepage = "https://rpaleoclim.joeroe.io"
	cran = "rpaleoclim" 

	version("1.0.1", md5="ba73a18a4af3778846b3e1583fb5fe88")

	depends_on("r-curl", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-terra@1.5.12:", type=("build", "run"))
