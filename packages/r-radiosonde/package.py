# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRadiosonde(RPackage):
	"""Tools for Plotting Skew-T Diagrams and Wind Profiles

	A
        collection of programs for 
        plotting SKEW-T,log p diagrams and wind profiles for data
        collected by radiosondes (the typical weather balloon-borne
        instrument). The format of this plot with companion lines to
	assess atmospheric stability are both standard  in meteorology
	and difficult to create from basic graphics functions. Hence
	this package. One novel feature is being able add several
	profiles to the same plot for comparison. 
	Use "help(ExampleSonde)" for an explanation of the variables
	needed and how they should be named in a data frame. See
	<https://github.com/dnychka/Radiosonde> for the package home page. 	
	"""
	
	cran = "RadioSonde" 

	version("4.2", md5="072c756f64e271a76cda2094ae02d262")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
