# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSuessr(RPackage):
	"""Suess and Laws Corrections for Marine Stable Carbon Isotope Data

	Generates region-specific Suess and Laws corrections for 
    stable carbon isotope data from marine organisms collected between 1850 and 2022. Version
    0.1.5 of 'SuessR' contains four built-in regions: the Bering Sea ('Bering Sea'), the
    Aleutian archipelago ('Aleutian Islands'), the Gulf of Alaska ('Gulf of Alaska'), and the 
    subpolar North Atlantic ('Subpolar North Atlantic'). Users can supply their own environmental 
    data for regions currently not built into the package to generate corrections for those regions.
	"""
	
	cran = "SuessR" 

	version("0.1.5", md5="dc5cddabf52df3e8f20d076f30c810c6")

	depends_on("r@3.5:", type=("build", "run"))
