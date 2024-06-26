# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRhdf5filters(RPackage):
	"""HDF5 Compression Filters.

	Provides a collection of compression filters for use with HDF5 datasets."""

	bioc = "rhdf5filters"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/rhdf5filters_1.14.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/rhdf5filters/rhdf5filters_1.14.1.tar.gz"]
	version("1.8.0", commit="b0b588b71a5595b30f4e698a50b84310dc19745d")
	version("1.6.0", commit="5f7f3a5b7dabd6e7d0c50cda70290e2472ff4f53")
	version("1.2.0", commit="25af0180f926b4b3ea11b30ec9277d26ad3d56b3")
	version("1.14.1", md5="3ecb2d30759fee6bde37bbb1f90fbf79")
	version("1.12.0", commit="4deabdef71c0349c4eaf7e5604cb7f389809f006")
	version("1.10.0", commit="6131538e2c5896dca0af33882bc2da961d79e49a")

	depends_on("r-rhdf5lib", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))

	def configure_args(self):
		args = []
		if self.spec.target.family == "aarch64":
			args.append("ax_cv_gcc_check_x86_cpu_init=yes")
			args.append("ax_cv_gcc_x86_cpu_supports_sse2=no")
		return args
