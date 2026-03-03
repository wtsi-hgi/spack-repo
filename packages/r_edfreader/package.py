# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REdfreader(RPackage):
	"""Reading EDF(+) and BDF(+) Files

	Reads European Data Format files EDF and EDF+, see <http://www.edfplus.info>,
    BioSemi Data Format files BDF, see <http://www.biosemi.com/faq/file_format.htm>,
    and BDF+ files, see <http://www.teuniz.net/edfbrowser/bdfplus%20format%20description.html>.
    The files are read in two steps: first the header is read
    and then the signals (using the header object as a parameter).
	"""
	
	cran = "edfReader" 

	version("1.2.1", md5="b97b881988b3fc6f03b46111302f55ed")

	depends_on("r@3.2:", type=("build", "run"))
