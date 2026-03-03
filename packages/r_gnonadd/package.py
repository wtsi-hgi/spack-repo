# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGnonadd(RPackage):
	"""Various Non-Additive Models for Genetic Associations

	The goal of 'gnonadd' is to simplify workflows in the analysis of non-additive effects of sequence variants. This includes variance effects (Ivarsdottir et. al (2017) <doi:10.1038/ng.3928>), correlation effects, interaction effects and dominance effects. The package also includes convenience functions for visualization.
	"""
	
	homepage = "https://github.com/DecodeGenetics/gnonadd"
	cran = "gnonadd" 

	version("1.0.2", md5="cef667b53e882c8a59b66257f5be8edd")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
