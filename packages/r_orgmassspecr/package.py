# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrgmassspecr(RPackage):
	"""Organic Mass Spectrometry

	Organic/biological mass spectrometry data analysis.
	"""
	
	homepage = "http://OrgMassSpec.github.io/"
	cran = "OrgMassSpecR" 

	version("0.5-3", md5="37ae3ef0245548c68d6b3aef7832832f")

	depends_on("r@3:", type=("build", "run"))
