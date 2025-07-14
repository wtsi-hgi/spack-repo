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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/SpectralTAD_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/SpectralTAD/SpectralTAD_1.18.0.tar.gz"]

	version("1.24.0", tag="RELEASE_3_21")
	version("1.18.0", sha256="7810bba38b494ac35662d4a32894fa787ca334f4a408687500edfd3f2c914238")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-primme", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-hiccompare", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
