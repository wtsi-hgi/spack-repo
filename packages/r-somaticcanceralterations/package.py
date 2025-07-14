# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSomaticcanceralterations(RPackage):
	"""Somatic Cancer Alterations

	Collection of somatic cancer alteration datasets
	"""
	
	bioc = "SomaticCancerAlterations"

	version("1.44.0", commit="4c474daeb55ae17512d9ecb01cd966692f7839c8")
	version("1.38.0", commit="37a1303a4c638e070094f40098db4b7922688f8b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))

