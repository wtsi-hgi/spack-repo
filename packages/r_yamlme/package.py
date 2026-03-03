# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYamlme(RPackage):
	"""Writing 'YAML' Headers for 'R-Markdown' Documents

	Setting layout through 'YAML' headers in 'R-Markdown' documents,
    enabling their automatic generation.
    Functions and methods may summarize 'R' objects in automatic reports, for
    instance check-lists and further reports applied to the packages 'taxlist'
    and 'vegtable'.
	"""
	
	homepage = "https://github.com/kamapu/yamlme"
	cran = "yamlme" 

	version("0.1.2", md5="373f8b91a5d99122bde3fc221eab9fe5")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("pandoc@1.14:", type=("build", "link", "run"))
