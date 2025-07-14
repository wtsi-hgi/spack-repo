# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsbackendmsp(RPackage):
	"""Mass Spectrometry Data Backend for NIST msp Files

	Mass spectrometry (MS) data backend supporting import and handling of MS/MS spectra from NIST MSP Format (msp) files. Import of data from files with different MSP *flavours* is supported. Objects from this package add support for MSP files to Bioconductor's Spectra package. This package is thus not supposed to be used without the Spectra package that provides a complete infrastructure for MS data handling.
	"""
	
	homepage = "https://github.com/RforMassSpectrometry/MsBackendMsp"
	bioc = "MsBackendMsp" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MsBackendMsp_1.6.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MsBackendMsp/MsBackendMsp_1.6.0.tar.gz"]

    version("1.12.0", tag="RELEASE_3_21")
	version("1.6.0", sha256="9e748bd8066416c0c2b9f8ba39cd3253ce755c0e45f6af6ae5eb095b9fa666fc")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-spectra@1.5.14:", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-mscoreutils", type=("build", "run"))
