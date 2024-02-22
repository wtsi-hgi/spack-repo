# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLmompi(RPackage):
	"""(Precipitation) Frequency Analysis and Variability with
L-Moments from 'lmom'

	It is an extension of 'lmom' R package: 'pel...()','cdf...()',qua...()' function
    families are lumped and called from one function per each family respectively in order to
    create robust automatic tools to fit data  with different probability
    distributions and then to estimate probability values and return periods.  The implemented functions are able to manage time series with constant and/or missing values without stopping
    the execution with error messages. The package also contains tools to  calculate several  indices based on variability (e.g. 'SPI' , Standardized
    Precipitation Index, see <https://climatedataguide.ucar.edu/climate-data/standardized-precipitation-index-spi> and <http://spei.csic.es/>) for multiple time series or spatially gridded values. 
	"""
	
	cran = "lmomPi" 

	version("0.6.6", md5="4aa6b946ba3a073ae8b745306e0e9f54")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-lmom", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
