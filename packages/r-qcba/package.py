# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQcba(RPackage):
	"""Quantitative Classification by Association Rules

	CBA postprocessing algorithm that creates smaller models for datasets containing quantitative (numerical) attributes. Article describing QCBA is published in Tomas Kliegr (2017) <arXiv:1711.10166>. The package can also postprocess results of the SBRL package, which is no longer in CRAN, but can be obtained from <https://github.com/cran/sbrl>.
	"""
	
	homepage = "https://github.com/kliegr/QCBA"
	cran = "qCBA" 

	version("0.5.1", md5="3b59a4d3cf0151bf56972b01bc8ec520")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-arules@1.6.6:", type=("build", "run"))
	depends_on("r-rjava@0.5.0:", type=("build", "run"))
	depends_on("r-arc@1.2:", type=("build", "run"))
	depends_on("openjdk@8:", type=("build", "link", "run"))
