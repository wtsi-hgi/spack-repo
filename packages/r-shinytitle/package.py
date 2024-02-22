# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinytitle(RPackage):
	"""Update Browser Window Title in 'shiny' Session

	Enables the ability to change or flash the title of the browser window during a 'shiny' session.
	"""
	
	homepage = "https://github.com/ashbaldry/shinytitle"
	cran = "shinytitle" 

	version("0.1.0", md5="1e89d52a34f6c511c475002a05a08074")

	depends_on("r-shiny", type=("build", "run"))
