# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAquaenv(RPackage):
	"""Integrated Development Toolbox for Aquatic Chemical Model
Generation

	Toolbox for the experimental aquatic chemist, focused on 
        acidification and CO2 air-water exchange. It contains all elements to
        model the pH, the related CO2 air-water exchange, and
        aquatic acid-base chemistry for an arbitrary marine,
        estuarine or freshwater system. It contains a suite of tools for 
        sensitivity analysis, visualisation, modelling of chemical batches, 
        and can be used to build dynamic models of aquatic systems. 
        As from version 1.0-4, it also contains functions to calculate 
        the buffer factors. 
	"""
	
	cran = "AquaEnv" 

	version("1.0-4", md5="e429401dd10645ddcbcdd01847cb677a")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
