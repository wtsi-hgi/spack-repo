# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIdslMxp(RPackage):
	"""Parser for mzML, mzXML, and netCDF Files (Mass Spectrometry
Data)

	A tiny parser to extract mass spectra data and metadata table of mass spectrometry acquisition properties from mzML, mzXML and netCDF files introduced in <doi:10.1021/acs.jproteome.2c00120>.
	"""
	
	homepage = "https://github.com/idslme/idsl.mxp"
	cran = "IDSL.MXP" 

	version("2.0", md5="65efa42f8212d136c5b06ed2ac641d8c")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
