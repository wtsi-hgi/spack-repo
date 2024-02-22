# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMkclass(RPackage):
	"""Statistical Classification

	Performance measures and scores for statistical classification such as accuracy, sensitivity, specificity, recall, similarity coefficients, AUC, GINI index, Brier score and many more. Calculation of optimal cut-offs and decision stumps (Iba and Langley (1991), <doi:10.1016/B978-1-55860-247-2.50035-8>) for all implemented performance measures. Hosmer-Lemeshow goodness of fit tests (Lemeshow and Hosmer (1982), <doi:10.1093/oxfordjournals.aje.a113284>; Hosmer et al (1997), <doi:10.1002/(SICI)1097-0258(19970515)16:9%3C965::AID-SIM509%3E3.0.CO;2-O>). Statistical and epidemiological risk measures such as relative risk, odds ratio, number needed to treat (Porta (2014), <doi:10.1093%2Facref%2F9780199976720.001.0001>).
	"""
	
	homepage = "https://github.com/stamats/MKclass"
	cran = "MKclass" 

	version("0.5", md5="a2930bf993bb827884d8ff2f7415134f")

	depends_on("r@4:", type=("build", "run"))
