# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGge(RPackage):
	"""Genotype Plus Genotype-by-Environment Biplots

	Create biplots for GGE (genotype plus genotype-by-environment) and
    GGB (genotype plus genotype-by-block-of-environments) models. 
    See Laffont et al. (2013) <doi:10.2135/cropsci2013.03.0178>.
	"""
	
	homepage = "https://kwstat.github.io/gge/"
	cran = "gge" 

	version("1.8", md5="a9744e1f67872f0c2488fd4d62998c02")

	depends_on("r-nipals", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
