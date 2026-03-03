# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAgreementinterval(RPackage):
	"""Agreement Interval of Two Measurement Methods

	A tool for calculating agreement interval of two measurement methods (Jason Liao (2015) <DOI:10.1515/ijb-2014-0030>) and present results in plots with discordance rate and/or clinically meaningful limit to quantify agreement quality.
	"""
	
	cran = "AgreementInterval" 

	version("0.1.1", md5="357846bc76a5cd68ef20f48a1a289669")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
