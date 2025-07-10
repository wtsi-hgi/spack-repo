# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCardinalworkflows(RPackage):
	"""Datasets and workflows for the Cardinal mass spectrometry imaging package

	Datasets and workflows for Cardinal: DESI and MALDI examples including pig fetus, cardinal painting, and human RCC.
	"""
	
	bioc = "CardinalWorkflows" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/CardinalWorkflows_1.34.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/CardinalWorkflows/CardinalWorkflows_1.34.0.tar.gz"]

	version("1.34.0", sha256="4b8f208696ac00fd875aabdf9a631a25022546e967dec3493d4a7813a7ffdf33")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cardinal", type=("build", "run"))

