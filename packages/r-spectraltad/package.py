# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpectraltad(RPackage):
	"""SpectralTAD: Hierarchical TAD detection using spectral clustering

	SpectralTAD is an R package designed to identify Topologically Associated Domains (TADs) from Hi-C contact matrices. It uses a modified version of spectral clustering that uses a sliding window to quickly detect TADs. The function works on a range of different formats of contact matrices and returns a bed file of TAD coordinates. The method does not require users to adjust any parameters to work and gives them control over the number of hierarchical levels to be returned.
	"""
	
	homepage = "https://github.com/dozmorovlab/SpectralTAD"
	bioc = "SpectralTAD"

	version("1.24.0", commit="d81c6a1e69b2d6ff4981f75700c2d4c11e0fc768")
	version("1.18.0", commit="380dfcd9f98c269bcac6f6226da54e6d21b27cfd")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-primme", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-hiccompare", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
