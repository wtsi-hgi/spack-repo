# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCuratedadipoarray(RPackage):
	"""A Curated Microarrays Dataset of MDI-induced Differentiated Adipocytes (3T3-L1) Under Genetic and Pharmacological Perturbations

	A curated dataset of Microarrays samples. The samples are MDI- induced pre-adipocytes (3T3-L1) at different time points/stage of differentiation under different types of genetic (knockdown/overexpression) and pharmacological (drug treatment) perturbations. The package documents the data collection and processing. In addition to the documentation, the package contains the scripts that was used to generated the data.
	"""
	
	homepage = "https://github.com/MahShaaban/curatedAdipoArray"
	bioc = "curatedAdipoArray" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/curatedAdipoArray_1.14.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/curatedAdipoArray/curatedAdipoArray_1.14.0.tar.gz"]

	version("1.14.0", md5="109be77c099e9d7b6da437577f619a54")

	depends_on("r@4:", type=("build", "run"))

	# experiment