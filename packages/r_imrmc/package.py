# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImrmc(RPackage):
	"""Multi-Reader, Multi-Case Analysis Methods (ROC, Agreement, and
Other Metrics)

	
  Do Multi-Reader, Multi-Case (MRMC) analyses of data from imaging studies where clinicians (readers)
  evaluate patient images (cases). What does this mean? ... Many imaging studies are designed
  so that every reader reads every case in all modalities, a fully-crossed study. In this case, the
  data is cross-correlated, and we consider the readers and cases to be cross-correlated random effects.
  An MRMC analysis accounts for the variability and correlations from the readers and cases when
  estimating variances, confidence intervals, and p-values. The functions in this package can treat
  arbitrary study designs and studies with missing data, not just fully-crossed study designs.
  The initial package analyzes the reader-average area under the receiver operating characteristic (ROC)
  curve with U-statistics according to Gallas, Bandos, Samuelson,
  and Wagner 2009 <doi:10.1080/03610920802610084>.
  Additional functions analyze other endpoints with U-statistics (binary performance
  and score differences) following the work by Gallas, Pennello, and Myers 2007
  <doi:10.1364/JOSAA.24.000B70>.
  Package development and documentation is at <https://github.com/DIDSR/iMRMC/tree/master>.
	"""
	
	cran = "iMRMC" 

	version("1.2.5", md5="0239c7c5700e9ea083b80910186bed8b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("openjdk@1.8:", type=("build", "link", "run"))
