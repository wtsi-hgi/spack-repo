# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFscache(RPackage):
	"""File System Cache

	Manages a file system cache. Regular files can be moved or copied to the cache folder. Sub-folders can be created in order to organize the files. Files can be located inside the cache using a glob function. Text contents can be easily stored in and retrieved from the cache using dedicated functions. It can be used for an application or a package, as a global cache, or as a per-user cache, in which case the standard OS user cache folder will be used (e.g.: on Linux $HOME/.cache/R/my_app_or_pkg_cache_folder).
	"""
	
	homepage = "https://gitlab.com/dbapis/r-fscache"
	cran = "fscache" 

	version("1.0.2", md5="1da9b29c04d844a82a6814aa2aa4a8ca")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-chk", type=("build", "run"))
	depends_on("r-lgr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
