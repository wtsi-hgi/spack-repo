# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAntiprofiles(RPackage):
	"""Implementation of gene expression anti-profiles

	Implements gene expression anti-profiles as described in Corrada Bravo et al., BMC Bioinformatics 2012, 13:272 doi:10.1186/1471-2105-13-272.
	"""
	
	homepage = "https://github.com/HCBravoLab/antiProfiles"
	bioc = "antiProfiles" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/antiProfiles_1.42.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/antiProfiles/antiProfiles_1.42.0.tar.gz"]

	version("1.48.0", tag="RELEASE_3_21")
	version("1.42.0", sha256="04905d3f407cd1968678937aef63859f37f03528102bde53caa9da8700f69f92")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-matrixstats@0.50:", type=("build", "run"))
	depends_on("r-locfit@1.5:", type=("build", "run"))
