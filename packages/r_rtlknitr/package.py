# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtlknitr(RPackage):
	"""Right to Left Dynamic Documents Using 'knitr'

	Provide seamless support for right-to-left (RTL) languages, such as Persian and Arabic, in R Markdown documents and 'LaTeX' output. It includes functions and hooks that enable easy integration of RTL language content, allowing users to create documents that adhere to RTL writing conventions. For in-depth insights into dynamic documents and the 'knitr' package, consider referring to Xie, Y (2014) <ISBN: 978-1-482-20353-0>.
	"""
	
	homepage = "https://github.com/FoadEsmaeili5/RTLknitr"
	cran = "RTLknitr" 

	version("1.0.0", md5="ecf0e3e2261588aa81864e0488322f8a")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-gt", type=("build", "run"))
	depends_on("r-bookdown", type=("build", "run"))
