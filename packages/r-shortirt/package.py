# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShortirt(RPackage):
	"""Procedures Based on Item Response Theory Models for the
Development of Short Test Forms

	Implement different Item Response Theory (IRT) based procedures for the development of static short test forms (STFs) from a test. Two main procedures are considered, specifically the typical IRT-based procedure for the development of STF, and a recently introduced procedure (Epifania, Anselmi & Robusto, 2022 <doi:10.1007/978-3-031-27781-8_7>).
        The procedures differ in how the most informative items are selected for the inclusion in the STF, either by considering their item information functions without considering any specific level of the latent trait (typical procedure) or by considering their informativeness with respect to specific levels of the latent trait, denoted as theta targets (the newly introduced procedure). Regarding the latter procedure, three methods are implemented for the definition of the theta targets: (i) theta targets are defined by segmenting the latent trait in equal intervals and considering the midpoint of each interval (equal interval procedure, eip), (ii) by clustering the latent trait to obtain unequal intervals and considering the centroids of the clusters as the theta targets (unequal intervals procedure, uip), and (iii) by letting the user set the specific theta targets of interest (user-defined procedure, udp).
        For further details on the procedure, please refer to Epifania, Anselmi & Robusto (2022) <doi:10.1007/978-3-031-27781-8_7>.
	"""
	
	cran = "shortIRT" 

	version("0.1.3", md5="22a3a3aa1a64d20f8461700327eab8f4")

	depends_on("r-tam", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
