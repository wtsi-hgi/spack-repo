# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSwatches(RPackage):
	"""Read, Inspect, and Manipulate Color Swatch Files

	There are numerous places to create and download color
    palettes. These are usually shared in 'Adobe' swatch file formats of
    some kind. There is also often the need to use standard palettes
    developed within an organization to ensure that aesthetics are carried over
    into all projects and output. Now there is a way to read these swatch
    files in R and avoid transcribing or converting color values by hand or
    or with other programs. This package provides functions to read and
    inspect 'Adobe Color' ('ACO'), 'Adobe Swatch Exchange' ('ASE'), 'GIMP Palette' ('GPL'),
    'OpenOffice' palette ('SOC') files and 'KDE Palette' ('colors') files. Detailed
    descriptions of 'Adobe Color' and 'Swatch Exchange' file formats as well as other
    swatch file formats can be found at
    <http://www.selapa.net/swatches/colors/fileformats.php>.
	"""
	
	homepage = "https://github.com/hrbrmstr/swatches"
	cran = "swatches" 

	version("0.5.0", md5="04e31e8986d288ba484f2c69f03cb9f9")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-pack", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
