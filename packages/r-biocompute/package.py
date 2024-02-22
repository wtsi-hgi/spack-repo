# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiocompute(RPackage):
	"""Create and Manipulate BioCompute Objects

	Tools to create, validate, and export BioCompute Objects
    described in King et al. (2019) <doi:10.17605/osf.io/h59uh>.
    Users can encode information in data frames, and compose
    BioCompute Objects from the domains defined by the standard.
    A checksum validator and a JSON schema validator are provided.
    This package also supports exporting BioCompute Objects as JSON,
    PDF, HTML, or 'Word' documents, and exporting to cloud-based platforms.
	"""
	
	homepage = "https://sbg.github.io/biocompute/"
	cran = "biocompute" 

	version("1.1.1", md5="3681410e1cf95e052b0d727012a54ef6")

	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
	depends_on("r-jsonvalidate", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
