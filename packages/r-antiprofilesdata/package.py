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

	version("1.44.0", commit="56cc43476bef726e35fedf38567a829665216f7a")
	version("1.38.0", commit="c6c3ef5ae1cbf5e51df8ffae7e820d4a79bd72f4")

	depends_on("r-biobase", type=("build", "run"))

