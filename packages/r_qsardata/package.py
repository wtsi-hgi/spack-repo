# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQsardata(RPackage):
	"""Quantitative Structure Activity Relationship (QSAR) Data Sets

	Molecular descriptors and outcomes for several public domain data sets
	"""
	
	homepage = "http://qsardata.r-forge.r-project.org/"
	cran = "QSARdata" 

	version("1.3", md5="5a1e33c00e8d5b1e86e374ee595eed71")

	depends_on("r@2.10:", type=("build", "run"))
