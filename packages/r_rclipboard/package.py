# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRclipboard(RPackage):
	"""Shiny/R Wrapper for 'clipboard.js'

	Leverages the functionality of 'clipboard.js', a JavaScript library
    for HMTL5-based copy to clipboard from web pages (see <https://clipboardjs.com>
    for more information), and provides a reactive copy-to-clipboard UI button 
    component, called 'rclipButton', and a a reactive copy-to-clipboard UI link 
    component, called 'rclipLink', for 'shiny' R applications.
	"""
	
	homepage = "https://github.com/sbihorel/rclipboard/"
	cran = "rclipboard" 

	version("0.2.1", md5="46158939710bc85e294fdc5f29461ee9")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-bslib@0.5.1:", type=("build", "run"))
