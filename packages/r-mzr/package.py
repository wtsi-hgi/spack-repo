# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMzr(RPackage):
	"""parser for netCDF, mzXML, mzData and mzML and mzIdentML files (mass
	spectrometry data).

	mzR provides a unified API to the common file formats and parsers
	available for mass spectrometry data. It comes with a wrapper for the
	ISB random access parser for mass spectrometry mzXML, mzData and mzML
	files. The package contains the original code written by the ISB, and a
	subset of the proteowizard library for mzML and mzIdentML. The netCDF
	reading code has previously been used in XCMS."""

	bioc = "mzR"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/mzR_2.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/mzR/mzR_2.36.0.tar.gz"]
    version("2.42.0", tag="RELEASE_3_21")
	version("2.36.0", sha256="084e6874232c940492135186262ce1232b2a664ac3126b2efc2d7b9dcc9dcc7c")
	version("2.34.0", commit="14ccc37ab3efd4b6003442a0268668258ccb7df9")
	version("2.32.0", commit="ef57d59205398558898a748ba9c8de66b0bddb81")
	version("2.30.0", commit="563ae755cfc7de1ac8862247779182b7b3aebdcc")
	version("2.28.0", commit="bee7d6fb5f99e1fab5444ae1ad27b0bc6e83be9e")
	version("2.24.1", commit="e1d4de8761e6729fd45320d842691c8fe9116b7b")
	version("2.18.1", commit="13f9f9b1149859c3e29cfce941d958cc4f680546")
	version("2.16.2", commit="22d7dad98f46b5bed7f6f7b3a703dcdf5997f709")
	version("2.14.0", commit="bf1154bc45101d95b5a67c66980856a779b84bd4")
	version("2.12.0", commit="f05eb27ae31c3d019cca10fc3b9ee513cbcdfc5a")
	version("2.10.0", commit="a6168b68e48c281e88de9647254a8db1e21df388")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocgenerics@0.13.6:", type=("build", "run"))
	depends_on("r-protgenerics@1.17.3:", type=("build", "run"))
	depends_on("r-ncdf4", type=("build", "run"))
	depends_on("r-rhdf5lib@1.1.4:", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))
