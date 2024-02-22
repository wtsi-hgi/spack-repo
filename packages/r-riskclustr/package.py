# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRiskclustr(RPackage):
	"""Functions to Study Etiologic Heterogeneity

	A collection of functions related to the study of etiologic heterogeneity both across disease subtypes and across individual disease markers. The included functions allow one to quantify the extent of etiologic heterogeneity in the context of a case-control study, and provide p-values to test for etiologic heterogeneity across individual risk factors. Begg CB, Zabor EC, Bernstein JL, Bernstein L, Press MF, Seshan VE (2013) <doi:10.1002/sim.5902>.
	"""
	
	homepage = "https://www.emilyzabor.com/riskclustr/"
	cran = "riskclustr" 

	version("0.4.1", md5="02a233c58e1c97b38ff2fe4c50dcedf1")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-mlogit", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
