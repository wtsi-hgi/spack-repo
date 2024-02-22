# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhenolocrop(RPackage):
	"""Time-Series Models to the Crop Phenology

	Fit a time-series model 
    to a crop phenology data, such as time-series rice canopy height.
    This package returns the model parameters as the summary statistics of crop phenology,
    and these parameters will be useful to characterize the growth pattern of each cultivar and 
    predict manually-measured traits, such as days to heading and biomass.
    Please see Taniguchi et al. (2022) <doi:10.3389/fpls.2022.998803> for detail.
    This package has been designed for scientific use.  
    Use for commercial purposes shall not be allowed.
	"""
	
	cran = "phenolocrop" 

	version("0.0.2", md5="56b6c942178c36c68483ce186a3667b0")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
