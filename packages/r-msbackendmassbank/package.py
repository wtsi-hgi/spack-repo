# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsbackendmassbank(RPackage):
	"""Mass Spectrometry Data Backend for MassBank record Files

	Mass spectrometry (MS) data backend supporting import and export of MS/MS library spectra from MassBank record files. Different backends are available that allow handling of data in plain MassBank text file format or allow also to interact directly with MassBank SQL databases. Objects from this package are supposed to be used with the Spectra Bioconductor package. This package thus adds MassBank support to the Spectra package.
	"""
	
	homepage = "https://github.com/RforMassSpectrometry/MsBackendMassbank"
	bioc = "MsBackendMassbank" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/MsBackendMassbank_1.10.1.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/MsBackendMassbank/MsBackendMassbank_1.10.1.tar.gz"]

	version("1.10.1", md5="a929aebecff77108bc62891bc397f057")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-spectra@1.9.12:", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-protgenerics", type=("build", "run"))
	depends_on("r-mscoreutils", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
