# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNtss(RPackage):
	"""Nonparametric Tests in Spatial Statistics

	Nonparametric test of independence between a pair of spatial objects
    (random fields, point processes) based on random shifts with torus or variance correction. See
    Mrkvička et al. (2021) <doi:10.1016/j.spasta.2020.100430>,
    Dvořák et al. (2022) <doi:10.1111/insr.12503>,
    Dvořák and Mrkvička (2022) <arxiv:2210.05424>.
	"""
	
	cran = "NTSS" 

	version("0.1.2", md5="abc9edeb5d4ab24dcf0a7bdbdf84c4ff")

	depends_on("r-spatstat", type=("build", "run"))
	depends_on("r-spatstat-random", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-spatstat-model", type=("build", "run"))
	depends_on("r-spatstat-explore", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
	depends_on("r-get", type=("build", "run"))
	depends_on("r-geor", type=("build", "run"))
