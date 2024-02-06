# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLanguageserver(RPackage):
	"""Language Server Protocol

	An implementation of the Language Server Protocol
    for R. The Language Server protocol is used by an editor client to
    integrate features like auto completion. See
    <https://microsoft.github.io/language-server-protocol/> for details.
	"""
	
	homepage = "https://github.com/REditorSupport/languageserver/"
	cran = "languageserver" 

	version("0.3.16", md5="c677e83e118b14921110df3e354babfb")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-callr@3:", type=("build", "run"))
	depends_on("r-collections@0.3:", type=("build", "run"))
	depends_on("r-fs@1.3.1:", type=("build", "run"))
	depends_on("r-jsonlite@1.6:", type=("build", "run"))
	depends_on("r-lintr@3:", type=("build", "run"))
	depends_on("r-r6@2.4.1:", type=("build", "run"))
	depends_on("r-roxygen2@7:", type=("build", "run"))
	depends_on("r-stringi@1.1.7:", type=("build", "run"))
	depends_on("r-styler@1.5.1:", type=("build", "run"))
	depends_on("r-xml2@1.2.2:", type=("build", "run"))
	depends_on("r-xmlparsedata@1.0.3:", type=("build", "run"))
