# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBarcoder(RPackage):
	"""Label Creation for Tracking and Collecting Data from Biological
Samples

	Tools to generate unique identifier codes and
    printable barcoded labels for the management of biological samples.
    The creation of unique ID codes and printable PDF files can be
    initiated by standard commands, user prompts, or through a GUI addin
    for R Studio. Biologically informative codes can be included for
    hierarchically structured sampling designs.
	"""
	
	homepage = "https://docs.ropensci.org/baRcodeR/"
	cran = "baRcodeR" 

	version("0.1.7", md5="5bf5a4b05cbf187496db70f4a34d7390")

	depends_on("r-qrcode", type=("build", "run"))
	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dt@0.3:", type=("build", "run"))
	depends_on("r-miniui@0.1.1:", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-shiny@0.13:", type=("build", "run"))
