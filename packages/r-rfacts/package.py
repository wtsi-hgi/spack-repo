# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRfacts(RPackage):
	"""R Interface to 'FACTS' on Unix-Like Systems

	The 'rfacts' package is an R interface to the
  Fixed and Adaptive Clinical Trial Simulator ('FACTS')
  on Unix-like systems. It programmatically invokes 'FACTS' to run clinical
  trial simulations, and it aggregates simulation output data
  into tidy data frames. These capabilities provide end-to-end
  automation for large-scale simulation pipelines, and
  they enhance computational reproducibility.
  For more information on 'FACTS' itself,
  please visit <https://www.berryconsultants.com/software/>.
	"""
	
	homepage = "https://elilillyco.github.io/rfacts/"
	cran = "rfacts" 

	version("0.2.1", md5="1c4b55bf21cee3d5f17526803d1b68f1")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-digest@0.6.25:", type=("build", "run"))
	depends_on("r-fs@1.3.1:", type=("build", "run"))
	depends_on("r-tibble@2.1.3:", type=("build", "run"))
	depends_on("r-xml2@1.2.2:", type=("build", "run"))
	depends_on("mono@5.20.1.19:", type=("build", "link", "run"))
