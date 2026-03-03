# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBigdawg(RPackage):
	"""Case-Control Analysis of Multi-Allelic Loci

	Data sets and functions for chi-squared Hardy-Weinberg and case-control association tests of highly polymorphic genetic data [e.g., human leukocyte antigen (HLA) data]. Performs association tests at multiple levels of polymorphism (haplotype, locus and HLA amino-acids) as described in Pappas DJ, Marin W, Hollenbach JA, Mack SJ (2016) <doi:10.1016/j.humimm.2015.12.006>. Combines rare variants to a common class to account for sparse cells in tables as described by Hollenbach JA, Mack SJ, Thomson G, Gourraud PA (2012) <doi:10.1007/978-1-61779-842-9_14>.
	"""
	
	homepage = "http://tools.immunogenomics.org/"
	cran = "BIGDAWG" 

	version("3.0.3", md5="95aebb9d8738b57364956d1209a57539")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-haplo-stats", type=("build", "run"))
