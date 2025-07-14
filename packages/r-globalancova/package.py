# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlobalancova(RPackage):
	"""Global test for groups of variables via model comparisons

	The association between a variable of interest (e.g. two groups) and the global pattern of a group of variables (e.g. a gene set) is tested via a global F-test. We give the following arguments in support of the GlobalAncova approach: After appropriate normalisation, gene-expression-data appear rather symmetrical and outliers are no real problem, so least squares should be rather robust. ANCOVA with interaction yields saturated data modelling e.g. different means per group and gene. Covariate adjustment can help to correct for possible selection bias. Variance homogeneity and uncorrelated residuals cannot be expected. Application of ordinary least squares gives unbiased, but no longer optimal estimates (Gauss-Markov-Aitken). Therefore, using the classical F-test is inappropriate, due to correlation. The test statistic however mirrors deviations from the null hypothesis. In combination with a permutation approach, empirical significance levels can be approximated. Alternatively, an approximation yields asymptotic p-values. The framework is generalized to groups of categorical variables or even mixed data by a likelihood ratio approach. Closed and hierarchical testing procedures are supported. This work was supported by the NGFN grant 01 GR 0459, BMBF, Germany and BMBF grant 01ZX1309B, Germany.
	"""
	
	bioc = "GlobalAncova" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GlobalAncova_4.20.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GlobalAncova/GlobalAncova_4.20.0.tar.gz"]

	version("4.26.0", tag="RELEASE_3_21")
	version("4.20.0", sha256="d031048e770b87e999e67039e47d817a70bb438748d71691316e6bf909503548")

	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-globaltest", type=("build", "run"))
	depends_on("r-annotate", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-dendextend", type=("build", "run"))
	depends_on("r-gseabase", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
