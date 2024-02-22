# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExiftoolr(RPackage):
	"""ExifTool Functionality from R

	Reads, writes, and edits EXIF and other file metadata
    using ExifTool <https://exiftool.org/>, returning read results as
    a data frame. ExifTool supports many different metadata formats
    including EXIF, GPS, IPTC, XMP, JFIF, GeoTIFF, ICC Profile,
    Photoshop IRB, FlashPix, AFCP and ID3, Lyrics3, as well as the
    maker notes of many digital cameras by Canon, Casio, DJI, FLIR,
    FujiFilm, GE, GoPro, HP, JVC/Victor, Kodak, Leaf,
    Minolta/Konica-Minolta, Motorola, Nikon, Nintendo, Olympus/Epson,
    Panasonic/Leica, Pentax/Asahi, Phase One, Reconyx, Ricoh, Samsung,
    Sanyo, Sigma/Foveon and Sony.
	"""
	
	homepage = "https://github.com/JoshOBrien/exiftoolr#readme"
	cran = "exiftoolr" 

	version("0.2.3", md5="01b815a3b89ac965ff514609baaf3c8a")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-backports", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-zip", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("perl", type=("build", "link", "run"))
