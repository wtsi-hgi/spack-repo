# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGovdown(RPackage):
	"""GOV.UK Style Templates for R Markdown

	A suite of custom R Markdown formats and templates
    for authoring web pages styled with the GOV.UK Design System.
	"""
	
	homepage = "https://ukgovdatascience.github.io/govdown/"
	cran = "govdown" 

	version("0.10.1", md5="47783e4bdc110fd18bf4a61ef9dde91d")

	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("pandoc@2.0:", type=("build", "link", "run"))
