# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPushoverr(RPackage):
	"""Send Push Notifications using 'Pushover'

	Send push notifications to mobile devices or the desktop
    using 'Pushover' <https://pushover.net>. These notifications can
    display things such as results, job status, plots, or any other text
    or numeric data.
	"""
	
	homepage = "https://briandconnelly.github.io/pushoverr/"
	cran = "pushoverr" 

	version("1.1.0", md5="d3ec550ee8240343f4304144ba61d923")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
