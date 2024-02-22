# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUkbnmr(RPackage):
	"""Removal of Unwanted Technical Variation from UK Biobank NMR
Metabolomics Biomarker Data

	A suite of utilities for working with the UK Biobank 
    <https://www.ukbiobank.ac.uk/> Nuclear Magnetic Resonance spectroscopy (NMR) 
    metabolomics data <https://biobank.ndph.ox.ac.uk/showcase/label.cgi?id=220>. 
    Includes functions for extracting biomarkers from decoded UK Biobank field 
    data, removing unwanted technical variation from biomarker concentrations,
    computing an extended set of lipid, fatty acid, and cholesterol fractions, 
    and for re-deriving composite biomarkers and ratios after adjusting data 
    for unwanted biological variation. For further details on methods see
    Ritchie SC et al. Sci Data (2023) <doi:10.1038/s41597-023-01949-y>.
	"""
	
	cran = "ukbnmr" 

	version("2.2", md5="52b7a11a359d664a1d582f879969630c")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-bit64", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
