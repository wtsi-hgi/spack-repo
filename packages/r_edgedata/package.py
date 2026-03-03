# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REdgedata(RPackage):
	"""Datasets that Support the EDGE Server DIY Logic

	Datasets from most recent CCIIO DIY entry
  in a tidy format. These support the Centers for Medicare and Medicaid
  Services' (CMS) risk adjustment Do-It-Yourself (DIY) process, which allows
  health insurance issuers to calculate member risk profiles under the Health
  and Human Services-Hierarchical Condition Categories (HHS-HCC) regression
  model. This regression model is used to calculate risk adjustment transfers.
  Risk adjustment is a selection mitigation program implemented under the
  Patient Protection and Affordable Care Act (ACA or Obamacare) in the USA.
  Under the ACA, health insurance issuers submit claims data to CMS	in order
  for CMS to calculate a risk score under the HHS-HCC regression model.
  However, CMS does not inform issuers of their average risk score until after
  the data submission deadline. These data sets can be used by issuers to
  calculate their average risk score mid-year. More information about risk
  adjustment and the HHS-HCC model can be found here:
  <https://www.cms.gov/mmrr/Articles/A2014/MMRR2014_004_03_a03.html>.
	"""
	
	cran = "edgedata" 

	version("0.2.0", md5="df9f19dbb851629f85a2c23d8aba0fd8")

	depends_on("r@4:", type=("build", "run"))
