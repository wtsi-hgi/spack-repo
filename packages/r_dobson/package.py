# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDobson(RPackage):
	"""Data from the GLM Book by Dobson and Barnett

	Example datasets from the book "An Introduction to Generalised Linear Models" (Year: 2018, ISBN:9781138741515) by Dobson and Barnett.
	"""
	
	cran = "dobson" 

	version("0.4", md5="f1dabf67b28c7ae4f3532fe1657043dc")

	depends_on("r@2.10:", type=("build", "run"))
