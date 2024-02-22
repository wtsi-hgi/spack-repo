# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExif(RPackage):
	"""Read EXIF Metadata from JPEGs

	Extracts Exchangeable Image File Format (EXIF) metadata, such as camera make and model, ISO speed and the date-time
             the picture was taken on, from JPEG images. Incorporates the 'easyexif' (https://github.com/mayanklahiri/easyexif)
             library.
	"""
	
	homepage = "https://github.com/Ironholds/exif"
	cran = "exif" 

	version("0.1.0", md5="9cedf675bbac2f85b6464141bf5f7257")

	depends_on("r-rcpp", type=("build", "run"))
