# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRdstreeboot(RPackage):
	"""RDS Tree Bootstrap Method

	A tree bootstrap method for estimating uncertainty in respondent-driven samples (RDS). Quantiles are estimated by multilevel resampling in such a way that preserves the dependencies of and accounts for the high variability of the RDS process.
	"""
	
	cran = "RDStreeboot" 

	version("1.0", md5="cc253ac87726fe799724af696f7f626c")

