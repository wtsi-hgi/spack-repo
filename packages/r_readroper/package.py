# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReadroper(RPackage):
	"""Simply Read ASCII Single and Multicard Polling Datasets

	A convenient way to read fixed-width ASCII polling datasets from providers like the Roper Center <https://ropercenter.cornell.edu>.
	"""
	
	cran = "readroper" 

	version("0.9.3", md5="eb8512002877eb13ef76ad4a5f889da4")

	depends_on("r-readr@1.3.1:", type=("build", "run"))
