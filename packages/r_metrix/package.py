# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetrix(RPackage):
	"""Water Quality Metrics Calculator

	Calculate different metrics based on aquatic
    macroinvertebrate density data (individuals per square meter) to
    assess water quality (Prat N et al. 2009).
	"""
	
	cran = "metrix" 

	version("1.1.0", md5="26fc9ce7bed324a3ca90508e7fc8702a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
