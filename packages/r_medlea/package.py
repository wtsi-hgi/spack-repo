# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMedlea(RPackage):
	"""Morphological and Structural Features of Medicinal Leaves

	Contains a dataset of morphological and structural features of 'Medicinal LEAves (MedLEA)'. The features of each species is recorded by manually viewing the medicinal plant repository available at (<http://www.instituteofayurveda.org/plants/>). You can also download repository of leaf images of 1099 medicinal plants in Sri Lanka.
	"""
	
	cran = "MedLEA" 

	version("1.0.2", md5="fef9e95c4423d79415b42dafb33791f8")

	depends_on("r@3.5:", type=("build", "run"))
