# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaqcsubsetilm(RPackage):
	"""MAQC data subset for the Illumina platform

	MAQC data subset for the Illumina platform
	"""
	
	bioc = "MAQCsubsetILM" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/MAQCsubsetILM_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/MAQCsubsetILM/MAQCsubsetILM_1.40.0.tar.gz"]

	version("1.40.0", md5="1c975db69a86cc80e99c5245998ee255")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))
	depends_on("r-lumi", type=("build", "run"))

	# experiment