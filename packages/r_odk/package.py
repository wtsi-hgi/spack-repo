# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROdk(RPackage):
	"""Convert 'ODK' or 'XLSForm' to 'SPSS' Data Frame

	After develop a 'ODK' <https://opendatakit.org/> frame, we can link the frame to 'Google Sheets' <https://www.google.com/sheets/about/> and collect data through 'Android' <https://www.android.com/>. This data uploaded to a 'Google sheets'. odk2spss() function help to convert the 'odk' frame into 'SPSS' <https://www.ibm.com/analytics/us/en/technology/spss/> frame. Also able to add downloaded 'Google sheets' data or read data from 'Google sheets' by using 'ODK' frame 'submission_url'.
	"""
	
	cran = "odk" 

	version("1.5", md5="2d1c7a0e52286c73ad1fa4055f7f0099")

	depends_on("r@3.4.1:", type=("build", "run"))
	depends_on("r-gsheet", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
