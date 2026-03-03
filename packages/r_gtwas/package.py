# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGtwas(RPackage):
	"""Genome and Transcriptome Wide Association Study

	Quantitative trait loci mapping and genome wide association analysis are used to find candidate molecular marker or region associated with phenotype based on linkage analysis and linkage disequilibrium. Gene expression quantitative trait loci mapping is used to find candidate molecular marker or region associated with gene expression. In this package, we applied the method in Liu W. (2011) <doi:10.1007/s00122-011-1631-7> and Gusev A. (2016) <doi:10.1038/ng.3506> to genome and transcriptome wide association study, which is aimed at revealing the association relationship between phenotype and molecular markers, expression levels, molecular markers nested within different related expression effect and expression effect nested within different related molecular marker effect. F test based on full and reduced model are performed to obtain p value or likelihood ratio statistic. The best linear model can be obtained by stepwise regression analysis.
	"""
	
	cran = "gtWAS" 

	version("1.1.0", md5="baf9047a962743e9f3d9f39635fad594")

	depends_on("r@2.10:", type=("build", "run"))
