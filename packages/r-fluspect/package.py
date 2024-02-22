# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFluspect(RPackage):
	"""Fluspect-B

	A model for leaf fluorescence, reflectance and transmittance spectra. It implements
    the model introduced by Vilfan et al. (2016) <DOI:10.1016/j.rse.2016.09.017>. Fluspect-B
    calculates the emission of ChlF on both the illuminated and shaded side of the leaf.
    Other input parameters are chlorophyll and carotenoid concentrations, leaf water, dry matter 
    and senescent material (brown pigments) content, leaf mesophyll structure parameter and ChlF 
    quantum efficiency for the two photosystems, PS-I and PS-II.
	"""
	
	cran = "fluspect" 

	version("1.0.0", md5="2ebc82666bc5e5ac7127bad490dd4507")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
