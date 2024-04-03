# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBslib(RPackage):
	"""Custom 'Bootstrap' 'Sass' Themes for 'shiny' and 'rmarkdown'.

	Simplifies custom 'CSS' styling of both 'shiny' and 'rmarkdown' via
	'Bootstrap' 'Sass'. Supports both 'Bootstrap' 3 and 4 as well as their
	various 'Bootswatch' themes. An interactive widget is also provided for
	previewing themes in real time."""

	cran = "bslib"

	license("MIT")

	version("0.6.1", md5="688035c1317d99324ef73bb5100664b1")
	version("0.4.2", sha256="9a40b7a1bbe409af273e1e940d921ab198ea576548f06f055f552f70ff822f19")
	version("0.4.1", sha256="4ebd1fc84cd19b414e8f8c13fb95270fc28ede125b6e58b08c574ca8c9e0e62f")
	version("0.4.0", sha256="fbea4ecec726f23618e825624f1d9c03939f765ca5a490b171ebf95b815475c2")
	version("0.3.1", sha256="5f5cb56e5cab9039a24cd9d70d73b69c2cab5b2f5f37afc15f71dae0339d9849")
	version("0.7.0", md5="081e2345dcf8260e89fd196f399e996b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-cachem", type=("build", "run"))
	depends_on("r-fastmap@1.1.1:", type=("build", "run"))
	depends_on("r-htmltools@0.5.8:", type=("build", "run"))
	depends_on("r-jquerylib@0.1.3:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-memoise@2.0.1:", type=("build", "run"))
	depends_on("r-mime", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sass@0.4.9:", type=("build", "run"))
