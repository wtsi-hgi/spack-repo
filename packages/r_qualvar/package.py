# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQualvar(RPackage):
	"""Implements Indices of Qualitative Variation Proposed by Wilcox
(1973)

	Implements indices of qualitative variation proposed by Wilcox
    (1973).
	"""
	
	homepage = "http://joelgombin.github.io/qualvar/"
	cran = "qualvar" 

	version("0.2.0", md5="f19d972c9906904e6cdf887d8370dedb")

	depends_on("r@2.10:", type=("build", "run"))
