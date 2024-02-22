# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDhsic(RPackage):
	"""Independence Testing via Hilbert Schmidt Independence Criterion

	Contains an implementation of the
	     d-variable Hilbert Schmidt independence criterion
	     and several hypothesis tests based on it, as described
	     in Pfister et al. (2017) <doi:10.1111/rssb.12235>.
	"""
	
	cran = "dHSIC" 

	version("2.1", md5="2ae4287774e5f665d07cb7b0d685947e")

	depends_on("r-rcpp", type=("build", "run"))
