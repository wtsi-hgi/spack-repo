# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RColoc(RPackage):
	"""Colocalisation Tests of Two Genetic Traits

	Performs the colocalisation tests described in
    Giambartolomei et al (2013) <doi:10.1371/journal.pgen.1004383>,
    Wallace (2020) <doi:10.1371/journal.pgen.1008720>,
    Wallace (2021) <doi:10.1371/journal.pgen.1009440>.
	"""
	
	homepage = "https://github.com/chr1swallace/coloc"
	cran = "coloc" 

	version("5.2.3", md5="d3498985773c1ac4d7984348ebe9b83d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-susier@0.12.6:", type=("build", "run"))
