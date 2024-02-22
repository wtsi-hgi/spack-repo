# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPkdata(RPackage):
	"""Creates Pharmacokinetic/Pharmacodynamic (PK/PD) Data

	Prepare pharmacokinetic/pharmacodynamic (PK/PD) data for PK/PD analyses. 
    This package provides functions to standardize infusion and bolus dose data while
    linking it to drug level or concentration data.
	"""
	
	cran = "pkdata" 

	version("0.1.0", md5="c0d873409f18c955477e417da4c39322")

	depends_on("r-lubridate", type=("build", "run"))
