# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArchive(RPackage):
	"""Multi-Format Archive and Compression Support

	Bindings to 'libarchive' <http://www.libarchive.org> the
	Multi-format archive and compression library. Offers R connections and
	direct extraction for many archive formats including 'tar', 'ZIP',
	'7-zip', 'RAR', 'CAB' and compression formats including 'gzip',
	'bzip2', 'compress', 'lzma' and 'xz'.
	"""
	
	homepage = "https://archive.r-lib.org/"
	cran = "archive"

	version("1.1.7", md5="f3504e5b4704312ce00d704d1e186083")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-cpp11", type=("build", "run"))
	depends_on("libarchive", type=("build", "link", "run"))
