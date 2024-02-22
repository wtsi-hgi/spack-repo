# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQrcode(RPackage):
	"""Generate QRcodes with R

	Create static QR codes in R. The content of the QR code is
    exactly what the user defines. We don't add a redirect URL, making it
    impossible for us to track the usage of the QR code. This allows to
    generate fast, free to use and privacy friendly QR codes.
	"""
	
	homepage = "https://thierryo.github.io/qrcode/"
	cran = "qrcode" 

	version("0.2.2", md5="41777731c8d903feefab96bb06cb6b38")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
