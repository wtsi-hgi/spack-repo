# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLifecourse(RPackage):
	"""Quantification of Lifecourse Fluidity

	Provides in built datasets and three functions.
  These functions are mobility_index, nonStanTest and linkedLives.  The mobility_index
  function facilitates the calculation of lifecourse fluidity, whilst the nonStanTest and the 
  linkedLives functions allow the user to determine the probability that the observed sequence data 
  was due to chance.  The linkedLives function acknowledges the fact that some individuals may
  have identical sequences.
  The datasets available provide sequence data on marital status(maritalData) 
  and mobility (mydata) for a selected group of individuals from the British Household Panel Study
  (BHPS).  In addition, personal and house ID's for 100 individuals are provided in a 
  third dataset (myHouseID) from the BHPS. 
	"""
	
	cran = "lifecourse" 

	version("2.0", md5="c94405a034cc153360df4f70dcc7dea4")

	depends_on("r-traminer", type=("build", "run"))
