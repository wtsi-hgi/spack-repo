# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsbackendmgf(RPackage):
	"""Mass Spectrometry Data Backend for Mascot Generic Format (mgf) Files

	Mass spectrometry (MS) data backend supporting import and export of MS/MS spectra data from Mascot Generic Format (mgf) files. Objects defined in this package are supposed to be used with the Spectra Bioconductor package. This package thus adds mgf file support to the Spectra package.
	"""
	
	homepage = "https://github.com/RforMassSpectrometry/MsBackendMgf"
	bioc = "MsBackendMgf"

	version("1.16.0", commit="680dc1348a9d74c15166624d38f15a13b4351a8d")
	version("1.10.0", commit="afaba38297fcc781753e803b56a961ab894d7f44")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-spectra@1.5.14:", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-mscoreutils", type=("build", "run"))
