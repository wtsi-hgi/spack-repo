# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMilineage(RPackage):
	"""Association Tests for Microbial Lineages on a Taxonomic Tree

	A variety of association tests for microbiome data analysis including Quasi-Conditional Association Tests (QCAT) described in Tang Z.-Z. et al.(2017) <doi:10.1093/bioinformatics/btw804> and Zero-Inflated Generalized Dirichlet Multinomial (ZIGDM) tests described in Tang Z.-Z. & Chen G. (2017, submitted).
	"""
	
	cran = "miLineage" 

	version("2.1", md5="ba01a20cbbc195ffe42f984371c64733")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-geepack", type=("build", "run"))
