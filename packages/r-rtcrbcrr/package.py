# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtcrbcrr(RPackage):
	"""Repertoire Analysis of the Detected Clonotype

	The 'TRUST4' or 'MiXCR' is used to identify the clonotypes.
    The goal of 'rTCRBCRr' is to process the results from these clonotyping tools,
    and analyze the clonotype repertoire metrics based on chain names and IGH isotypes.
    The manuscript is still under preparation for publication for now.
    The references describing the methods in this package will be added later.
	"""
	
	cran = "rTCRBCRr" 

	version("0.1.1", md5="e4585fe14136e291b500e6da8ade6897")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
