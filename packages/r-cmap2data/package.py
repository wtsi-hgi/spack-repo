# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCmap2data(RPackage):
	"""Connectivity Map (version 2) Data

	Data package which provides default drug profiles for the DrugVsDisease package as well as associated gene lists and data clusters used by the DrugVsDisease package.
	"""
	
	bioc = "cMap2data" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/cMap2data_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/cMap2data/cMap2data_1.38.0.tar.gz"]

    version("1.44.0", tag="RELEASE_3_21")
	version("1.38.0", sha256="8d3b9a65860f5efad950e8619c02d47c173f715b5209601c282bf0815fda5eb4")

	depends_on("r@2.10:", type=("build", "run"))

