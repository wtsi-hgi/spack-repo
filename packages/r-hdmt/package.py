# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHdmt(RPackage):
	"""A Multiple Testing Procedure for High-Dimensional Mediation
Hypotheses

	A multiple-testing procedure for high-dimensional mediation hypotheses. Mediation analysis is of rising interest in epidemiology and clinical trials. Among existing methods for mediation analyses, the popular joint significance (JS) test yields an overly conservative type I error rate and therefore low power. In the R package 'HDMT' we implement a multiple-testing procedure that accurately controls the family-wise error rate (FWER) and the false discovery rate (FDR) when using JS for testing high-dimensional mediation hypotheses. The core of our procedure is based on estimating the proportions of three component null hypotheses and deriving the corresponding mixture distribution of null p-values. Results of the data examples include better-behaved quantile-quantile plots and improved detection of novel mediation relationships on the role of DNA methylation in genetic regulation of gene expression. With increasing interest in mediation by molecular intermediaries such as gene expression, the proposed method addresses an unmet methodological challenge. Methods used in the package refer to James Y. Dai, Janet L. Stanford & Michael LeBlanc (2020) <doi:10.1080/01621459.2020.1765785>.
	"""
	
	cran = "HDMT" 

	version("1.0.5", md5="a2081cf140e8a4bca8820c846fe8aa94")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-fdrtool", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
