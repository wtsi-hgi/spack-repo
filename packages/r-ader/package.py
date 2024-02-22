# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAder(RPackage):
	"""Data Analysis in Ecology

	Data sets used in Cayuela and De la Cruz (2022, ISBN:978-84-8476-833-3).
	"""
	
	homepage = "https://www.paraninfo.es/catalogo/9788484768333/"
	cran = "ADER" 

	version("1.5", md5="303fb07432f71961f2d91a3d72e09591")

	depends_on("r@3.5:", type=("build", "run"))
