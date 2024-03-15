# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRhtslib(RPackage):
	"""HTSlib high-throughput sequencing library as an R package.

	This package provides version 1.7 of the 'HTSlib' C library for high-
	throughput sequence analysis. The package is primarily useful to
	developers of other R packages who wish to make use of HTSlib.
	Motivation and instructions for use of this package are in the vignette,
	vignette(package="Rhtslib", "Rhtslib")."""

	bioc = "Rhtslib"

	# There is a problem with the git repository where the commit for
	# version 1.28.0 pulls changes to a file that blocks checking out the
	# commit. Use the branch instead.
	# error: Your local changes to the following files would be overwritten by
	# checkout:
	#			 src/htslib-1.15.1/htscodecs/tests/names/tok3/nv.names.1
	#			 Please, commit your changes or stash them before you can switch
	#			 branches.
	#			 Aborting
	# version("1.28.0", commit='214fde2218bdbca89f1e12a30d2e081e76915aef')
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Rhtslib_2.4.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Rhtslib/Rhtslib_2.4.1.tar.gz"]

	version("2.4.1", md5="b7d295a694e865f4f4060c94c4bca446")

	depends_on("r-zlibbioc", type=("build", "run"))
	depends_on("bzip2", type=("build", "link", "run"))
	depends_on("lzma", type=("build", "link", "run"))
	depends_on("xz", type=("build", "link", "run"))
	depends_on("curl", type=("build", "link", "run"))

	patch("use_spack_Makeconf.patch", when="@1.12:1.28.0")
	patch("find_deps-1.12.patch", when="@1.12:1.14")
	patch("find_deps-1.16.patch", when="@1.16:1.28.0")

	@when("@1.12:")
	def setup_build_environment(self, env):
		env.set("BZIP2_INCLUDE", self.spec["bzip2"].headers.include_flags)
		env.set("XZ_INCLUDE", self.spec["xz"].headers.include_flags)
		env.set("BZIP2_LIB", self.spec["bzip2"].libs.search_flags)
		env.set("XZ_LIB", self.spec["xz"].libs.search_flags)
