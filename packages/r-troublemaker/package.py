# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTroublemaker(RPackage):
	"""Generates Spatial Problems in R for 'AMPL'

	Provides methods for generating .dat files for use with the 'AMPL' 
    software using spatial data, particularly rasters. It includes support for 
    various spatial data formats and different problem types. By automating the 
    process of generating 'AMPL' datasets, this package can help streamline 
    optimization workflows and make it easier to solve complex optimization 
    problems. The methods implemented in this package are described in detail
    in a publication by Fourer et al. (<doi:10.1287/mnsc.36.5.519>).
	"""
	
	homepage = "https://github.com/Sustainscapes/TroublemakeR"
	cran = "TroublemakeR" 

	version("0.0.1", md5="e523573b397065eae6f4eb838536a9f8")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
