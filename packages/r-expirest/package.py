# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExpirest(RPackage):
	"""Expiry Estimation Procedures

	The Australian Regulatory Guidelines for Prescription
    Medicines (ARGPM), guidance on "Stability testing for prescription
    medicines", recommends to predict the shelf life of chemically derived
    medicines from stability data by taking the worst case situation at batch
    release into account. Consequently, if a change over time is observed,
    a release limit needs to be specified. Finding a release limit and the
    associated shelf life is supported, as well as the standard approach
    that is recommended by guidance Q1E "Evaluation of stability data"
    from the International Council for Harmonisation (ICH).
	"""
	
	homepage = "https://github.com/piusdahinden/expirest"
	cran = "expirest" 

	version("0.1.6", md5="9b9b85d5529c97fb042eafb8409af6a1")
	version("0.1.5", md5="86b56ea576906e10e361aa151d214a07")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
