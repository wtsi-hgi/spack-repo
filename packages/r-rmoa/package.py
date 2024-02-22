# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmoa(RPackage):
	"""Connect R with MOA for Massive Online Analysis

	Connect R with MOA (Massive Online Analysis -
    <https://moa.cms.waikato.ac.nz/>) to build classification models and
    regression models on streaming data or out-of-RAM data.
    Also streaming recommendation models are made available.
	"""
	
	homepage = "http://www.bnosac.be"
	cran = "RMOA" 

	version("1.1.0", md5="d36c613973a986b6885646bceae0794a")

	depends_on("r-rmoajars@1:", type=("build", "run"))
	depends_on("r-rjava@0.6.3:", type=("build", "run"))
	depends_on("openjdk@5:", type=("build", "link", "run"))
