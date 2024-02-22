# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExifr(RPackage):
	"""EXIF Image Data in R

	Reads EXIF data using ExifTool <https://exiftool.org>
    and returns results as a data frame.
    ExifTool is a platform-independent Perl library plus a command-line
    application for reading, writing and editing meta information in a wide variety
    of files. ExifTool supports many different metadata formats including EXIF,
    GPS, IPTC, XMP, JFIF, GeoTIFF, ICC Profile, Photoshop IRB, FlashPix, AFCP and
    ID3, as well as the maker notes of many digital cameras by Canon, Casio, FLIR,
    FujiFilm, GE, HP, JVC/Victor, Kodak, Leaf, Minolta/Konica-Minolta, Motorola, Nikon,
    Nintendo, Olympus/Epson, Panasonic/Leica, Pentax/Asahi, Phase One, Reconyx, Ricoh,
    Samsung, Sanyo, Sigma/Foveon and Sony.
	"""
	
	homepage = "https://github.com/paleolimbot/exifr"
	cran = "exifr" 

	version("0.3.2", md5="746c5147c9b2af5279388797ac97a81b")

	depends_on("r-curl", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("perl", type=("build", "link", "run"))
