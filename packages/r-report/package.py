# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReport(RPackage):
	"""Automated Reporting of Results and Statistical Models

	The aim of the 'report' package is to bridge the gap between
    R’s output and the formatted results contained in your manuscript.
    This package converts statistical models and data frames into textual
    reports suited for publication, ensuring standardization and quality
    in results reporting.
	"""
	
	homepage = "https://easystats.github.io/report/"
	cran = "report" 

	version("0.5.8", md5="65a93219aa8d8c633776013d57d4a151")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-bayestestr@0.13.1:", type=("build", "run"))
	depends_on("r-effectsize@0.8.6:", type=("build", "run"))
	depends_on("r-insight@0.19.7:", type=("build", "run"))
	depends_on("r-parameters@0.21.3:", type=("build", "run"))
	depends_on("r-performance@0.10.8:", type=("build", "run"))
	depends_on("r-datawizard@0.9:", type=("build", "run"))
