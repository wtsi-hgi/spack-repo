# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCinargenesets(RPackage):
	"""Ready-to-Use Curated Gene Sets for 'cinaR'

	Immune related gene sets provided along with the 'cinaR' package.
	"""
	
	homepage = "https://github.com/eonurk/cinaR-genesets"
	cran = "cinaRgenesets" 

	version("0.1.1", md5="f4f1691881f527594b1c07b323458487")

	depends_on("r@3.5:", type=("build", "run"))
