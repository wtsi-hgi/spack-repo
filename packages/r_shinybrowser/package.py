# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinybrowser(RPackage):
	"""Find Out Information About a User's Web Browser in 'Shiny'

	Sometimes it's useful to know some information about your user in a 'Shiny' app. The available
    information is: browser name (such as 'Chrome' or 'Safari') and version, device type 
    (mobile or desktop), operating system (such as 'Windows' or 'Mac' or 'Android') and version,
    and browser dimensions.
	"""
	
	homepage = "https://github.com/daattali/shinybrowser"
	cran = "shinybrowser" 

	version("1.0.0", md5="549d241efa393a23ebe715485a6fc09d")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-shiny@1.0.4:", type=("build", "run"))
