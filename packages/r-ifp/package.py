# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIfp(RPackage):
	"""Identifying Functional Polymorphisms

	A suite for identifying causal models using relative concordances and identifying causal polymorphisms in case-control genetic association data, especially with large controls re-sequenced data.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "IFP" 

	version("0.2.4", md5="14506f6cd41de21bce359fd0ef95be62")

	depends_on("r@2.11.1:", type=("build", "run"))
	depends_on("r-haplo-stats", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
