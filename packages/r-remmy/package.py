# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRemmy(RPackage):
	"""API Client for 'Lemmy'

	An HTTP API client for 'Lemmy'
    (<https://github.com/LemmyNet/lemmy>) in R. Code and documentation are
    generated from the official 'JavaScript' client source
    (<https://github.com/LemmyNet/lemmy-js-client>).
	"""
	
	homepage = "https://github.com/long39ng/remmy"
	cran = "remmy" 

	version("0.1.0", md5="b565cd80d1dc89b1bf91c3e2c133c245")

	depends_on("r-curl", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
