# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhysiology(RPackage):
	"""Calculate physiologic characteristics of awake and anesthetized
adults, children and infants

	A variety of formulae are provided for estimation
    of physiologic characteristics of infants, children, and adults.
    Calculations include: body surface area, ideal weight, airway
    dead-space, the alveolar gas equation, and GFR.  Each formula is
    referenced to the original publication. Future functions will cover
    more material with a focus on anaesthesia, critical care and
    peri-operative medicine.
	"""
	
	homepage = "https://jackwasey.github.io/physiology/"
	cran = "physiology" 

	version("1.2.1", md5="5fe85afd7c3ecb15ed74a130a282c336")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
