# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAntiprofilesdata(RPackage):
	"""Normal colon and cancer preprocessed affy data for antiProfile building.

	Colon normal tissue and cancer samples used in Corrada Bravo, et al. gene expression anti-profiles paper: BMC Bioinformatics 2012, 13:272 doi:10.1186/1471-2105-13-272. Measurements are z-scores obtained from the GeneExpression Barcode in the 'frma' package
	"""
	
	bioc = "antiProfilesData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/antiProfilesData_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/antiProfilesData/antiProfilesData_1.38.0.tar.gz"]

	version("1.44.0", tag="RELEASE_3_21")
	version("1.38.0", sha256="0be4952b30882ee6d3e883ba39d19b886cac6c195daf5c81bc3bc968f8196f59")

	depends_on("r-biobase", type=("build", "run"))

