# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNhsrdatasets(RPackage):
	"""NHS and Healthcare-Related Data for Education and Training

	Free United Kingdom National Health Service (NHS) and other healthcare, or population health-related data for education and training purposes. This package contains synthetic data based on real healthcare datasets, or cuts of open-licenced official data.  This package exists to support skills development in the NHS-R community: <https://nhsrcommunity.com/>.
	"""
	
	homepage = "https://github.com/nhs-r-community/NHSRdatasets"
	cran = "NHSRdatasets" 

	version("0.3.0", md5="6b1b9656527c11a4b7f884e7b3ed144d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
