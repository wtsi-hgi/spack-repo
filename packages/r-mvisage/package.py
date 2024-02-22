# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvisage(RPackage):
	"""Compute and Visualize Bivariate Associations

	Pearson and Spearman correlation coefficients are commonly used to quantify the strength
	of bivariate associations of genomic variables.  For example, correlations of gene-level 
	DNA copy number and gene expression measurements may be used to assess the impact of 
	DNA copy number changes on gene expression in tumor tissue.  'MVisAGe' enables users to 
	quickly compute and visualize the correlations in order to assess the effect of regional 
	genomic events such as changes in DNA copy number or DNA methylation level.  Please see
	Walter V, Du Y, Danilova L, Hayward MC, Hayes DN, 2018. Cancer Research 
	<doi:10.1158/0008-5472.CAN-17-3464>.
	"""
	
	cran = "MVisAGe" 

	version("0.2.1", md5="f24278b3c382da2053f230527c769520")

	depends_on("r@3.3.1:", type=("build", "run"))
