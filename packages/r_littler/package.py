# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLittler(RPackage):
	"""R at the Command-Line via 'r'

	A scripting and command-line front-end
 is provided by 'r' (aka 'littler') as a lightweight binary wrapper around
 the GNU R language and environment for statistical computing and graphics.
 While R can be used in batch mode, the r binary adds full support for
 both 'shebang'-style scripting (i.e. using a  hash-mark-exclamation-path
 expression as the first line in scripts) as well as command-line use in
 standard Unix pipelines. In other words, r provides the R language without
 the environment.
	"""
	
	homepage = "https://github.com/eddelbuettel/littler"
	cran = "littler" 

	version("0.3.20", md5="194f1116ebf52154948847b0acd5c76a")

	depends_on("bzip2", type=("build", "link", "run"))
	depends_on("icu4c", type=("build", "link", "run"))
	depends_on("libiconv", type=("build", "link", "run"))
	depends_on("xz", type=("build", "link", "run"))
	depends_on("zlib", type=("build", "link", "run"))
