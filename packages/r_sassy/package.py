# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSassy(RPackage):
	"""Makes 'R' Easier for Everyone

	A meta-package that aims to make 'R' easier for everyone, 
    especially programmers who have a background in 'SAS®' software.
    This set of packages brings many useful concepts to 'R', including
    data libraries, data dictionaries, formats 
    and format catalogs, a data step, and a traceable log.  The 'flagship'
    package is a reporting package that can output in text, rich text, 'PDF', 
    'HTML', and 'DOCX' file formats.
	"""
	
	homepage = "https://r-sassy.org"
	cran = "sassy" 

	version("1.2.3", md5="0ccc5117d1abf7cc337b6d4630d35847")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-fmtr@1.6.2:", type=("build", "run"))
	depends_on("r-common@1.1:", type=("build", "run"))
	depends_on("r-logr@1.3.4:", type=("build", "run"))
	depends_on("r-libr@1.2.8:", type=("build", "run"))
	depends_on("r-reporter@1.4.3:", type=("build", "run"))
	depends_on("r-procs@1.0.4:", type=("build", "run"))
