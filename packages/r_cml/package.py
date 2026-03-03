# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCml(RPackage):
	"""Conditional Manifold Learning

	Finds a low-dimensional embedding of high-dimensional data, conditioning on available manifold information. The current version supports conditional MDS (based on either conditional SMACOF in Bui (2021) <arXiv:2111.13646> or closed-form solution in Bui (2022) <doi:10.1016/j.patrec.2022.11.007>) and conditional ISOMAP in Bui (2021) <arXiv:2111.13646>.
	"""
	
	cran = "cml" 

	version("0.2.2", md5="6811ebc0da9d4564dc0f9722df403325")

	depends_on("r-vegan", type=("build", "run"))
