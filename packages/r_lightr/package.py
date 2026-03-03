# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLightr(RPackage):
	"""Read Spectrometric Data and Metadata

	Parse various reflectance/transmittance/absorbance spectra file
    formats to extract spectral data and metadata, as described in Gruson, White
    & Maia (2019) <doi:10.21105/joss.01857>. Among other formats, it can import
    files from 'Avantes' <https://www.avantes.com/>, 'CRAIC' 
    <https://www.microspectra.com/>, and 'OceanInsight' (formerly 'OceanOptics') 
    <https://www.oceaninsight.com/> brands.
	"""
	
	homepage = "https://docs.ropensci.org/lightr/"
	cran = "lightr" 

	version("1.7.1", md5="c09f96b2939429c7ad761dffae22e850")
	version("1.7.0", md5="6d736827d1550d694d694b7fc21628d8")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-xml2@1:", type=("build", "run"))
