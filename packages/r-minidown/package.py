# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMinidown(RPackage):
	"""Create Simple Yet Powerful HTML Documents with Light Weight CSS
Frameworks

	Create minimal, responsive, and style-agnostic HTML documents with
    the lightweight CSS frameworks such as 'sakura', 'Water.css', and 'spcss'.
    Powerful features include table of contents floating as a sidebar,
    folding codes and results, and more.
	"""
	
	homepage = "https://minidown.atusy.net"
	cran = "minidown" 

	version("0.4.0", md5="4724ec600f6df21ac7cba48d0c89e56a")

	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-katex", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-mime", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-sass", type=("build", "run"))
	depends_on("r-xfun", type=("build", "run"))
	depends_on("pandoc@2.7.2:", type=("build", "link", "run"))
