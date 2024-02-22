# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCms(RPackage):
	"""Calculate Medicare Reimbursement

	Uses the 'CMS' application programming interface <https://dnav.cms.gov/api/healthdata>
    to provide users databases containing yearly
    Medicare reimbursement rates in the United States. Data can be acquired
    for the entire United States or only for specific localities. Currently,
    support is only provided for the Medicare Physician Fee Schedule,
    but support will be expanded for other 'CMS' databases in future versions.
	"""
	
	homepage = "https://github.com/subramv/cms"
	cran = "cms" 

	version("0.1.0", md5="6a3b8507a2b3d66fa89c5ef5d1ae66b7")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-assertthat@0.2:", type=("build", "run"))
	depends_on("r-dplyr@0.8:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-readr@1.3:", type=("build", "run"))
	depends_on("r-rlang@0.4:", type=("build", "run"))
	depends_on("r-rvest@0.3:", type=("build", "run"))
	depends_on("r-xml2@1.3:", type=("build", "run"))
