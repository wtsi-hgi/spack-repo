# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmixpanel(RPackage):
	"""API for Mixpanel

	Provides an interface to many endpoints of Mixpanel's Data Export, Engage and JQL API. The R functions allow for event and profile data export as well as for segmentation, retention, funnel and addiction analysis. Results are always parsed into convenient R objects. Furthermore it is possible to load and update profiles. 
	"""
	
	homepage = "https://github.com/ploner/RMixpanel"
	cran = "RMixpanel" 

	version("0.7-1", md5="46dbee4c2f9e2113292a179d794ce7e3")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
