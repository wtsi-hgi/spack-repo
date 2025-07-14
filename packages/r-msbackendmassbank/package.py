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

	version("1.16.1", commit="1b552ef3a3b7c01edbb2bb9a4b8cfddd44100781")
	version("1.10.1", commit="21cf023852e656da90d2ae4e31db58074317161a")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-spectra@1.9.12:", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-protgenerics", type=("build", "run"))
	depends_on("r-mscoreutils", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
