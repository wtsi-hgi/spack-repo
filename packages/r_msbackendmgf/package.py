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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MsBackendMgf_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MsBackendMgf/MsBackendMgf_1.10.0.tar.gz"]

	version("1.10.0", md5="a8b5cc0b0f9c2da6222c217ae8a4c44f")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-spectra@1.5.14:", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-mscoreutils", type=("build", "run"))
