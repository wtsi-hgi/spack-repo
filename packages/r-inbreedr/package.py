# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInbreedr(RPackage):
	"""Analysing Inbreeding Based on Genetic Markers

	A framework for analysing inbreeding and heterozygosity-fitness
    correlations (HFCs) based on microsatellite and SNP markers.
	"""
	
	cran = "inbreedR" 

	version("0.3.3", md5="f19a63bdf5cecaaeb1067ab931af13b9")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-data-table@1.9.6:", type=("build", "run"))
