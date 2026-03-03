# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAcro(RPackage):
	"""A Tool for Automating the Statistical Disclosure Control of
Research Outputs

	Assists researchers and output checkers by distinguishing between research output that is safe to publish, output that requires further analysis, and output that cannot be published because of substantial disclosure risk. A paper about the tool was presented at The United Nations Economic Commission for Europe Expert Meeting on Statistical Data Confidentiality, see <https://unece.org/statistics/events/SDC2023> and <https://uwe-repository.worktribe.com/output/11060964>.
	"""
	
	cran = "acro"

	version("0.1.1", md5="666979e057e702c4d663ba1b8e6b9a32")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-admiraldev", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("python@3.8:", type=("build", "link", "run"))
