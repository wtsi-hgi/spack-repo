# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFacebookorganicr(RPackage):
	"""Get Data from 'Facebook Organic' via the 'Windsor.ai' API

	Collect  your data on digital marketing campaigns from 'Facebook Organic' using the 'Windsor.ai' API <https://windsor.ai/api-fields/>.
	"""
	
	homepage = "https://windsor.ai/"
	cran = "facebookorganicR" 

	version("0.1.0", md5="007e59ed3823b12e32153d0eb48505d2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-jsonlite@1.7.2:", type=("build", "run"))
