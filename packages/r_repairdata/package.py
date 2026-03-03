# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRepairdata(RPackage):
	"""Open Repair Alliance Datasets 2021

	The complete data set of open repair data, full compliant with the Open Repair Data Standards (ORDS).
      It combines the datasets contributed by partner organizations of the Open Repair Alliance (ORA). Last updated: 2021-02-22. 
      The package also contains via quests enriched datasets on batteries,
      printer, mobiles, and tablets.
	"""
	
	homepage = "https://github.com/petzi53/repairData"
	cran = "repairData" 

	version("0.1.0", md5="90784261939bac6ab66cc4464baadd88")

	depends_on("r@3.5:", type=("build", "run"))
