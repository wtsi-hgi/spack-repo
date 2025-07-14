# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsbackendrawfilereader(RPackage):
	"""Mass Spectrometry Backend for Reading Thermo Fisher Scientific raw Files

	implements a MsBackend for the Spectra package using Thermo Fisher Scientific's NewRawFileReader .Net libraries. The package is generalizing the functionality introduced by the rawrr package Methods defined in this package are supposed to extend the Spectra Bioconductor package.
	"""
	
	homepage = "https://github.com/fgcz/MsBackendRawFileReader"
	bioc = "MsBackendRawFileReader" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MsBackendRawFileReader_1.8.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MsBackendRawFileReader/MsBackendRawFileReader_1.8.1.tar.gz"]

    version("1.14.0", tag="RELEASE_3_21")
	version("1.8.1", sha256="6034696b2b131b8b2b55f8dca44a488adefd7daf41a6b00a452a95361820074e")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-spectra@1.5.8:", type=("build", "run"))
	depends_on("r-mscoreutils", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-rawrr@1.10.1:", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
