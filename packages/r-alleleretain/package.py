# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlleleretain(RPackage):
	"""Allele Retention, Inbreeding, and Demography

	Simulate the effect of management or demography on allele retention and inbreeding accumulation in bottlenecked populations of animals with overlapping generations.
	"""
	
	homepage = "https://sites.google.com/site/alleleretain/"
	cran = "AlleleRetain" 

	version("2.0.2", md5="057c494305e3ba96f7ad0012b12a3d83")

	depends_on("r@3.4:", type=("build", "run"))
