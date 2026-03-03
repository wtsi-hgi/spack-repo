# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQrencoder(RPackage):
	"""Quick Response Code (QR Code) / Matrix Barcode Creator

	Quick Response codes (QR codes) are a type of matrix bar code and can be
    used to authenticate transactions, provide access to multi-factor authentication
    services and enable general data transfer in an image. QR codes use four standardized 
    encoding modes (numeric, alphanumeric, byte/binary, and kanji) to efficiently store 
    data. Matrix barcode generation is performed efficiently in C via the included
    'libqrencoder' library created by Kentaro Fukuchi.
	"""
	
	homepage = "http://github.com/hrbrmstr/qrencoder"
	cran = "qrencoder" 

	version("0.1.0", md5="9657f8bc79e1f3039d5db04e18392ba4")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
