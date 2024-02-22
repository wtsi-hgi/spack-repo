# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDair(RPackage):
	"""Interface with Google Cloud Document AI API

	R interface for the Google Cloud Services 'Document AI API'
    <https://cloud.google.com/document-ai/> with additional tools for
    output file parsing and text reconstruction. 'Document AI' is a
    powerful server-based OCR service that extracts text and tables from
    images and PDF files with high accuracy. 'daiR' gives R users
    programmatic access to this service and additional tools to handle
    and visualize the output. See the package website <https://dair.info/>
    for more information and examples.
	"""
	
	homepage = "https://github.com/Hegghammer/daiR"
	cran = "daiR" 

	version("1.0.0", md5="612b385a16f4b35a762d5f610ee48e6f")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-beepr", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-gargle", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-googlecloudstorager", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("r-pdftools", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readtext", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
