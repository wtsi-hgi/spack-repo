# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMessaging(RPackage):
	"""Conveniently Issue Messages, Warnings, and Errors

	Provides tools for creating and issuing nicely-formatted
    text within R diagnostic messages and those messages given during
    warnings and errors. The formatting of the messages can be
    customized using templating features. Issues with singular and
    plural forms can be handled through specialized syntax.
	"""
	
	homepage = "https://github.com/rich-iannone/messaging"
	cran = "messaging" 

	version("0.1.0", md5="ecbe4bcc2715b7f24a5cf8804091030b")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-dplyr@0.7.4:", type=("build", "run"))
	depends_on("r-glue@1.2:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang@0.2:", type=("build", "run"))
	depends_on("r-stringr@1.3:", type=("build", "run"))
