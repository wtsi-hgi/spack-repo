# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRhdf5filters(RPackage):
	"""HDF5 Compression Filters.

	Provides a collection of compression filters for use with HDF5 datasets."""

	bioc = "rhdf5filters"

	license("BSD-2-Clause")
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/rhdf5filters_1.14.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/rhdf5filters/rhdf5filters_1.14.1.tar.gz"]

	version("1.14.1", md5="3ecb2d30759fee6bde37bbb1f90fbf79")

	depends_on("r-rhdf5lib", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))

	def configure_args(self):
		args = []
		if self.spec.target.family == "aarch64":
			args.append("ax_cv_gcc_check_x86_cpu_init=yes")
			args.append("ax_cv_gcc_x86_cpu_supports_sse2=no")
		return args
